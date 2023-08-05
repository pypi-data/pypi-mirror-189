// SPDX-FileCopyrightText: 2021-2022 Heiko Schaefer <heiko@schaefer.name>
// SPDX-License-Identifier: MIT OR Apache-2.0

//! Generate and import keys

use std::convert::TryFrom;
use std::time::{SystemTime, UNIX_EPOCH};

use crate::algorithm::{Algo, AlgoInfo, Curve, EccAttrs, RsaAttrs};
use crate::apdu::command::Command;
use crate::apdu::commands;
use crate::card_do::{ApplicationRelatedData, Fingerprint, KeyGenerationTime};
use crate::crypto_data::{
    CardUploadableKey, EccKey, EccPub, EccType, PrivateKeyMaterial, PublicKeyMaterial, RSAKey,
    RSAPub,
};
use crate::openpgp::OpenPgpTransaction;
use crate::tlv::{length::tlv_encode_length, value::Value, Tlv};
use crate::{apdu, Error, KeyType, Tag, Tags};

/// Generate asymmetric key pair on the card.
///
/// This is a convenience wrapper around gen_key() that:
/// - sets algorithm attributes (if not None)
/// - generates a key pair on the card
/// - sets the creation time on the card to the current host time
/// - calculates fingerprint for the key and sets it on the card
///
/// `fp_from_pub` calculates the fingerprint for a public key data object and
/// creation timestamp
pub(crate) fn gen_key_with_metadata(
    card_tx: &mut OpenPgpTransaction,
    fp_from_pub: fn(&PublicKeyMaterial, KeyGenerationTime, KeyType) -> Result<Fingerprint, Error>,
    key_type: KeyType,
    algo: Option<&Algo>,
) -> Result<(PublicKeyMaterial, KeyGenerationTime), Error> {
    // Set algo on card if it's Some
    if let Some(target_algo) = algo {
        // FIXME: caching
        let ard = card_tx.application_related_data()?; // no caching, here!
        let ecap = ard.extended_capabilities()?;

        // Only set algo if card supports setting of algo attr
        if ecap.algo_attrs_changeable() {
            card_tx.set_algorithm_attributes(key_type, target_algo)?;
        } else {
            // Check if the current algo on the card is the one we want, if
            // not we return an error.

            // NOTE: For RSA, the target algo shouldn't prescribe an
            // Import-Format. The Import-Format should always depend on what
            // the card supports.

            // let cur_algo = ard.get_algorithm_attributes(key_type)?;
            // assert_eq!(&cur_algo, target_algo);

            // FIXME: return error
        }
    }

    // get current (possibly updated) state of algo
    let ard = card_tx.application_related_data()?; // no caching, here!
    let cur_algo = ard.algorithm_attributes(key_type)?;

    // generate key
    let tlv = generate_asymmetric_key_pair(card_tx, key_type)?;

    // derive pubkey
    let pubkey = tlv_to_pubkey(&tlv, &cur_algo)?;

    log::trace!("public {:x?}", pubkey);

    // set creation time
    let time = SystemTime::now();

    // Store creation timestamp (unix time format, limited to u32)
    let ts = time
        .duration_since(UNIX_EPOCH)
        .map_err(|e| Error::InternalError(format!("This should never happen {}", e)))?
        .as_secs() as u32;

    let ts = ts.into();

    card_tx.set_creation_time(ts, key_type)?;

    // calculate/store fingerprint
    let fp = fp_from_pub(&pubkey, ts, key_type)?;
    card_tx.set_fingerprint(fp, key_type)?;

    Ok((pubkey, ts))
}

/// Transform a public key Tlv from the card into PublicKeyMaterial
fn tlv_to_pubkey(tlv: &Tlv, algo: &Algo) -> Result<PublicKeyMaterial, crate::Error> {
    let n = tlv.find(Tags::PublicKeyDataRsaModulus);
    let v = tlv.find(Tags::PublicKeyDataRsaExponent);

    let ec = tlv.find(Tags::PublicKeyDataEccPoint);

    match (n, v, ec) {
        (Some(n), Some(v), None) => {
            let rsa = RSAPub::new(n.serialize(), v.serialize());
            Ok(PublicKeyMaterial::R(rsa))
        }
        (None, None, Some(ec)) => {
            let data = ec.serialize();
            log::trace!("EC --- len {}, data {:x?}", data.len(), data);

            let ecc = EccPub::new(data, algo.clone());
            Ok(PublicKeyMaterial::E(ecc))
        }

        (_, _, _) => Err(Error::UnsupportedAlgo(format!(
            "Unexpected public key material from card {:?}",
            tlv
        ))),
    }
}

/// 7.2.14 GENERATE ASYMMETRIC KEY PAIR
///
/// This runs the low level key generation primitive on the card.
/// (This does not set algorithm attributes, creation time or fingerprint)
pub(crate) fn generate_asymmetric_key_pair(
    card_tx: &mut OpenPgpTransaction,
    key_type: KeyType,
) -> Result<Tlv, Error> {
    log::info!("OpenPgpTransaction: generate_asymmetric_key_pair");

    // generate key
    let crt = control_reference_template(key_type)?;
    let gen_key_cmd = commands::gen_key(crt.serialize().to_vec());

    let resp = apdu::send_command(card_tx.tx(), gen_key_cmd, true)?;
    resp.check_ok()?;

    let tlv = Tlv::try_from(resp.data()?)?;

    Ok(tlv)
}

/// Get the public key material for a key from the card.
///
/// ("Returns the public key of an asymmetric key pair previously generated
/// in the card or imported")
///
/// (See 7.2.14 GENERATE ASYMMETRIC KEY PAIR)
pub(crate) fn public_key(
    card_tx: &mut OpenPgpTransaction,
    key_type: KeyType,
) -> Result<PublicKeyMaterial, Error> {
    log::info!("OpenPgpTransaction: public_key");

    // get current algo
    let ard = card_tx.application_related_data()?; // FIXME: caching
    let algo = ard.algorithm_attributes(key_type)?;

    // get public key
    let crt = control_reference_template(key_type)?;
    let get_pub_key_cmd = commands::get_pub_key(crt.serialize().to_vec());

    let resp = apdu::send_command(card_tx.tx(), get_pub_key_cmd, true)?;
    resp.check_ok()?;

    let tlv = Tlv::try_from(resp.data()?)?;
    let pubkey = tlv_to_pubkey(&tlv, &algo)?;

    Ok(pubkey)
}

/// Import private key material to the card as a specific KeyType.
///
/// If the key is suitable for `key_type`, an Error is returned (either
/// caused by checks before attempting to upload the key to the card, or by
/// an error that the card reports during an attempt to upload the key).
pub(crate) fn key_import(
    card_tx: &mut OpenPgpTransaction,
    key: Box<dyn CardUploadableKey>,
    key_type: KeyType,
    algo_info: Option<AlgoInfo>,
) -> Result<(), Error> {
    log::info!("OpenPgpTransaction: key_import");

    // FIXME: caching?
    let ard = card_tx.application_related_data()?;

    let (algo, key_cmd) = match key.private_key()? {
        PrivateKeyMaterial::R(rsa_key) => {
            // RSA bitsize
            // (round up to 4-bytes, in case the key has 8+ leading zero bits)
            let rsa_bits = (((rsa_key.n().len() * 8 + 31) / 32) * 32) as u16;

            let rsa_attrs = determine_rsa_attrs(rsa_bits, key_type, &ard, algo_info)?;

            let key_cmd = rsa_key_import_cmd(key_type, rsa_key, &rsa_attrs)?;

            (Algo::Rsa(rsa_attrs), key_cmd)
        }
        PrivateKeyMaterial::E(ecc_key) => {
            let ecc_attrs =
                determine_ecc_attrs(ecc_key.oid(), ecc_key.ecc_type(), key_type, algo_info)?;

            let key_cmd = ecc_key_import_cmd(key_type, ecc_key, &ecc_attrs)?;

            (Algo::Ecc(ecc_attrs), key_cmd)
        }
    };

    let fp = key.fingerprint()?;

    // Now that we have marshalled all necessary information, perform all
    // set-operations on the card.

    // Only set algo attrs if "Extended Capabilities" lists the feature
    if ard.extended_capabilities()?.algo_attrs_changeable() {
        card_tx.set_algorithm_attributes(key_type, &algo)?;
    }

    apdu::send_command(card_tx.tx(), key_cmd, false)?.check_ok()?;
    card_tx.set_fingerprint(fp, key_type)?;
    card_tx.set_creation_time(key.timestamp(), key_type)?;

    Ok(())
}

/// Determine suitable RsaAttrs for the current card, for an `rsa_bits`
/// sized key.
///
/// If available, via lookup in `algo_info`, otherwise the current
/// algorithm attributes are checked. If neither method yields a
/// result, we 'guess' the RsaAttrs setting.
pub(crate) fn determine_rsa_attrs(
    rsa_bits: u16,
    key_type: KeyType,
    ard: &ApplicationRelatedData,
    algo_info: Option<AlgoInfo>,
) -> Result<RsaAttrs, crate::Error> {
    // Figure out suitable RSA algorithm parameters:

    // Does the card offer a list of algorithms?
    let rsa_attrs = if let Some(algo_info) = algo_info {
        // Yes -> Look up the parameters for key_type and rsa_bits.
        // (Or error, if the list doesn't have an entry for rsa_bits)
        card_algo_rsa(algo_info, key_type, rsa_bits)?
    } else {
        // No -> Get the current algorithm attributes for key_type.

        let algo = ard.algorithm_attributes(key_type)?;

        // Is the algorithm on the card currently set to RSA?
        if let Algo::Rsa(rsa) = algo {
            // If so, use the algorithm parameters from the card and
            // adjust the bit length based on the user-provided key.
            RsaAttrs::new(rsa_bits, rsa.len_e(), rsa.import_format())
        } else {
            // The card doesn't provide an algorithm list, and the
            // current algorithm on the card is not RSA.
            //
            // So we 'guess' a value for len_e (some cards only
            // support 17, others only support 32).

            // [If this approach turns out to be insufficient, we
            // need to determine the model of the card and use a
            // list of which RSA parameters that model of card
            // supports]

            RsaAttrs::new(rsa_bits, 32, 0)
        }
    };

    Ok(rsa_attrs)
}

/// Derive EccAttrs from `oid` and `ecc_type`, check if the OID is listed in
/// `algo_info`.
pub(crate) fn determine_ecc_attrs(
    oid: &[u8],
    ecc_type: EccType,
    key_type: KeyType,
    algo_info: Option<AlgoInfo>,
) -> Result<EccAttrs, crate::Error> {
    // If we have an algo_info, refuse upload if oid is not listed
    if let Some(algo_info) = algo_info {
        let algos = check_card_algo_ecc(algo_info, key_type, oid);
        if algos.is_empty() {
            // If oid is not in algo_info, return error.
            return Err(Error::UnsupportedAlgo(format!(
                "Oid {:?} unsupported according to algo_info",
                oid
            )));
        }

        // Note: Looking up ecc_type in the card's "Algorithm Information"
        // seems to do more harm than good, so we don't do it.
        // Some cards report erroneous information about supported algorithms
        // - e.g. YubiKey 5 reports support for EdDSA over Cv25519 and
        // Ed25519, but not ECDH.
        //
        // We do however, use import_format from algorithm information.

        if !algos.is_empty() {
            return Ok(EccAttrs::new(
                ecc_type,
                Curve::try_from(oid)?,
                algos[0].import_format(),
            ));
        }
    }

    // Return a default when we have no algo_info.
    // (Do cards that support ecc but have no algo_info exist?)

    Ok(EccAttrs::new(ecc_type, Curve::try_from(oid)?, None))
}

/// Look up RsaAttrs parameters in algo_info based on key_type and rsa_bits
fn card_algo_rsa(algo_info: AlgoInfo, key_type: KeyType, rsa_bits: u16) -> Result<RsaAttrs, Error> {
    // Find suitable algorithm parameters (from card's list of algorithms).

    // Get Algos for this keytype
    let keytype_algos: Vec<_> = algo_info.filter_by_keytype(key_type);
    // Get RSA algo attributes
    let rsa_algos: Vec<_> = keytype_algos
        .iter()
        .filter_map(|a| if let Algo::Rsa(r) = a { Some(r) } else { None })
        .collect();

    // Filter card algorithms by rsa bitlength of the key we want to upload
    let algo: Vec<_> = rsa_algos
        .iter()
        .filter(|&a| a.len_n() == rsa_bits)
        .collect();

    // Did we find a suitable algorithm entry?
    if !algo.is_empty() {
        // HACK: The SmartPGP applet reports two variants of RSA (import
        // format 1 and 3), but in fact only supports the second variant.
        // Using the last option happens to work better, in that case.
        Ok((**algo.last().unwrap()).clone())
    } else {
        // RSA with this bit length is not in algo_info
        Err(Error::UnsupportedAlgo(format!(
            "RSA {} unsupported according to algo_info",
            rsa_bits
        )))
    }
}

/// Get all entries from algo_info with matching `oid` and `key_type`.
fn check_card_algo_ecc(algo_info: AlgoInfo, key_type: KeyType, oid: &[u8]) -> Vec<EccAttrs> {
    // Find suitable algorithm parameters (from card's list of algorithms).

    // Get Algos for this keytype
    let keytype_algos: Vec<_> = algo_info.filter_by_keytype(key_type);

    // Get attributes
    let ecc_algos: Vec<_> = keytype_algos
        .iter()
        .filter_map(|a| if let Algo::Ecc(e) = a { Some(e) } else { None })
        .collect();

    // Find entries with this OID in the algorithm information for key_type
    ecc_algos
        .iter()
        .filter(|e| e.oid() == oid)
        .cloned()
        .cloned()
        .collect()
}

/// Create command for RSA key import
fn rsa_key_import_cmd(
    key_type: KeyType,
    rsa_key: Box<dyn RSAKey>,
    rsa_attrs: &RsaAttrs,
) -> Result<Command, Error> {
    // Assemble key command (see 4.4.3.12 Private Key Template)

    // Collect data for "Cardholder private key template" DO (7F48)
    //
    // (Describes the content of the Cardholder private key DO)
    let mut cpkt_data: Vec<u8> = vec![];

    // "Cardholder private key" (5F48)
    //
    // "The key data elements according to the definitions in the CPKT DO
    // (7F48)."
    let mut key_data = Vec::new();

    // -- Public exponent: e --
    cpkt_data.extend(Vec::from(Tags::PrivateKeyDataRsaPublicExponent));
    // Expected length of e in bytes, rounding up from the bit value in algo.
    let len_e_bytes = ((rsa_attrs.len_e() + 7) / 8) as u8;
    // len_e in bytes has a value of 3-4, it doesn't need TLV encoding
    cpkt_data.push(len_e_bytes);

    // Push e, padded with zero bytes from the left
    let e_as_bytes = rsa_key.e();

    if len_e_bytes as usize > e_as_bytes.len() {
        key_data.extend(vec![0; len_e_bytes as usize - e_as_bytes.len()]);
    }

    key_data.extend(e_as_bytes);

    // -- Prime1: p + Prime2: q --

    // len_p and len_q are len_n/2 (value from card algorithm list).
    // transform unit from bits to bytes.
    let len_p_bytes: u16 = rsa_attrs.len_n() / 2 / 8;
    let len_q_bytes: u16 = rsa_attrs.len_n() / 2 / 8;

    cpkt_data.extend(Vec::from(Tags::PrivateKeyDataRsaPrime1));
    // len p in bytes, TLV-encoded
    cpkt_data.extend_from_slice(&tlv_encode_length(len_p_bytes));

    cpkt_data.extend(Vec::from(Tags::PrivateKeyDataRsaPrime2));
    // len q in bytes, TLV-encoded
    cpkt_data.extend_from_slice(&tlv_encode_length(len_q_bytes));

    // FIXME: do p/q need to be padded from the left when many leading
    // bits are zero?
    key_data.extend(rsa_key.p().iter());
    key_data.extend(rsa_key.q().iter());

    // import format requires chinese remainder theorem fields
    if rsa_attrs.import_format() == 2 || rsa_attrs.import_format() == 3 {
        // PQ: 1/q mod p
        let pq = rsa_key.pq();
        cpkt_data.extend(Vec::from(Tags::PrivateKeyDataRsaPq));
        cpkt_data.extend(&tlv_encode_length(pq.len() as u16));
        key_data.extend(pq.iter());

        // DP1: d mod (p - 1)
        let dp1 = rsa_key.dp1();
        cpkt_data.extend(Vec::from(Tags::PrivateKeyDataRsaDp1));
        cpkt_data.extend(&tlv_encode_length(dp1.len() as u16));
        key_data.extend(dp1.iter());

        // DQ1: d mod (q - 1)
        let dq1 = rsa_key.dq1();
        cpkt_data.extend(Vec::from(Tags::PrivateKeyDataRsaDq1));
        cpkt_data.extend(&tlv_encode_length(dq1.len() as u16));
        key_data.extend(dq1.iter());
    }

    // import format requires modulus n field
    if rsa_attrs.import_format() == 1 || rsa_attrs.import_format() == 3 {
        let n = rsa_key.n();
        cpkt_data.extend(Vec::from(Tags::PrivateKeyDataRsaModulus));
        cpkt_data.extend(&tlv_encode_length(n.len() as u16));
        key_data.extend(n.iter());
    }

    // Assemble the DOs for upload
    let cpkt = Tlv::new(Tags::CardholderPrivateKeyTemplate, Value::S(cpkt_data));
    let cpk = Tlv::new(Tags::ConcatenatedKeyData, Value::S(key_data));

    // "Control Reference Template"
    let crt = control_reference_template(key_type)?;

    // "Extended header list (DO 4D)"
    let ehl = Tlv::new(Tags::ExtendedHeaderList, Value::C(vec![crt, cpkt, cpk]));

    // Return the full key import command
    Ok(commands::key_import(ehl.serialize().to_vec()))
}

/// Create command for ECC key import
fn ecc_key_import_cmd(
    key_type: KeyType,
    ecc_key: Box<dyn EccKey>,
    ecc_attrs: &EccAttrs,
) -> Result<Command, Error> {
    let private = ecc_key.private();

    // Collect data for "Cardholder private key template" DO (7F48)
    //
    // (Describes the content of the Cardholder private key DO)
    let mut cpkt_data = vec![];

    // "Cardholder private key" (5F48)
    //
    // "The key data elements according to the definitions in the CPKT DO
    // (7F48)."
    let mut key_data = Vec::new();

    // Process "scalar"
    cpkt_data.extend(Vec::from(Tags::PrivateKeyDataEccPrivateKey));
    cpkt_data.extend_from_slice(&tlv_encode_length(private.len() as u16));

    key_data.extend(private);

    // Process "public", if the import format requires it
    if ecc_attrs.import_format() == Some(0xff) {
        let p = ecc_key.public();

        cpkt_data.extend(Vec::from(Tags::PrivateKeyDataEccPublicKey));
        cpkt_data.extend_from_slice(&tlv_encode_length(p.len() as u16));

        key_data.extend(p);
    }

    // Assemble DOs

    // "Cardholder private key template"
    let cpkt = Tlv::new(Tags::CardholderPrivateKeyTemplate, Value::S(cpkt_data));

    // "Cardholder private key"
    let cpk = Tlv::new(Tags::ConcatenatedKeyData, Value::S(key_data));

    // "Control Reference Template"
    let crt = control_reference_template(key_type)?;

    // "Extended header list (DO 4D)" (contains the three inner TLV)
    let ehl = Tlv::new(Tags::ExtendedHeaderList, Value::C(vec![crt, cpkt, cpk]));

    // key import command
    Ok(commands::key_import(ehl.serialize().to_vec()))
}

/// Get "Control Reference Template" Tlv for `key_type`
fn control_reference_template(key_type: KeyType) -> Result<Tlv, Error> {
    // "Control Reference Template" (0xB8 | 0xB6 | 0xA4)
    let tag = match key_type {
        KeyType::Decryption => Tags::CrtKeyConfidentiality,
        KeyType::Signing => Tags::CrtKeySignature,
        KeyType::Authentication => Tags::CrtKeyAuthentication,
        KeyType::Attestation => {
            // The attestation key CRT looks like: [B6 03 84 01 81]
            //
            // This is a "Control Reference Template in extended format with Key-Ref".
            // (See "4.4.3.12 Private Key Template")
            let tlv = Tlv::new(
                Tags::CrtKeySignature,
                // Spec page 38: [..] to indicate the private key: "empty or 84 01 xx"
                Value::C(vec![Tlv::new(
                    Tag::from([0x84]),
                    // Spec page 43: "Key-Ref 0x81 is reserved for the Attestation key of Yubico."
                    Value::S(vec![0x81]),
                )]),
            );
            return Ok(tlv);
        }
    };
    Ok(Tlv::new(tag, Value::S(vec![])))
}
