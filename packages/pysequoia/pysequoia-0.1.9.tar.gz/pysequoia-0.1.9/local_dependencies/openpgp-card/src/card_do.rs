// SPDX-FileCopyrightText: 2021-2022 Heiko Schaefer <heiko@schaefer.name>
// SPDX-License-Identifier: MIT OR Apache-2.0

//! OpenPGP card data objects (DO)

use std::convert::{TryFrom, TryInto};
use std::fmt::{Display, Formatter, Write};
use std::time::{Duration, UNIX_EPOCH};

use chrono::{DateTime, Utc};

use crate::{algorithm::Algo, tlv::Tlv, Error, KeySet, KeyType, Tags};

mod algo_attrs;
mod algo_info;
mod application_id;
mod cardholder;
mod extended_cap;
mod extended_length_info;
mod fingerprint;
mod historical;
mod key_generation_times;
mod pw_status;

/// 4.4.3.1 Application Related Data
///
/// The "application related data" DO contains a set of DOs.
/// This struct offers read access to these DOs.
///
/// (Note: when any of the information in this DO changes on the card, you
/// need to re-read ApplicationRelatedData from the card to receive the
/// new values!)
pub struct ApplicationRelatedData(pub(crate) Tlv);

impl ApplicationRelatedData {
    /// Get application identifier (AID), ISO 7816-4
    pub fn application_id(&self) -> Result<ApplicationIdentifier, Error> {
        let aid = self.0.find(Tags::ApplicationIdentifier);

        if let Some(aid) = aid {
            Ok(ApplicationIdentifier::try_from(&aid.serialize()[..])?)
        } else {
            Err(Error::NotFound("Couldn't get Application ID.".to_string()))
        }
    }

    /// Get historical bytes
    pub fn historical_bytes(&self) -> Result<HistoricalBytes, Error> {
        let hist = self.0.find(Tags::HistoricalBytes);

        if let Some(hist) = hist {
            log::trace!("Historical bytes: {:x?}", hist);
            (hist.serialize().as_slice()).try_into()
        } else {
            Err(Error::NotFound(
                "Failed to get historical bytes.".to_string(),
            ))
        }
    }

    /// Get extended length information (ISO 7816-4), which
    /// contains maximum number of bytes for command and response.
    pub fn extended_length_information(&self) -> Result<Option<ExtendedLengthInfo>, Error> {
        let eli = self.0.find(Tags::ExtendedLengthInformation);

        log::trace!("Extended length information: {:x?}", eli);

        if let Some(eli) = eli {
            // The card has returned extended length information
            Ok(Some((&eli.serialize()[..]).try_into()?))
        } else {
            // The card didn't return this (optional) DO. That is ok.
            Ok(None)
        }
    }

    #[allow(dead_code)]
    fn general_feature_management() -> Option<bool> {
        unimplemented!()
    }

    #[allow(dead_code)]
    fn discretionary_data_objects() {
        unimplemented!()
    }

    /// Get extended Capabilities
    pub fn extended_capabilities(&self) -> Result<ExtendedCapabilities, Error> {
        let app_id = self.application_id()?;
        let version = app_id.version();

        // get from cached "application related data"
        let ecap = self.0.find(Tags::ExtendedCapabilities);

        if let Some(ecap) = ecap {
            Ok(ExtendedCapabilities::try_from((
                &ecap.serialize()[..],
                version,
            ))?)
        } else {
            Err(Error::NotFound(
                "Failed to get extended capabilities.".to_string(),
            ))
        }
    }

    /// Get algorithm attributes (for each key type)
    pub fn algorithm_attributes(&self, key_type: KeyType) -> Result<Algo, Error> {
        let aa = self.0.find(key_type.algorithm_tag());

        if let Some(aa) = aa {
            Algo::try_from(&aa.serialize()[..])
        } else {
            Err(Error::NotFound(format!(
                "Failed to get algorithm attributes for {:?}.",
                key_type
            )))
        }
    }

    /// Get PW status Bytes
    pub fn pw_status_bytes(&self) -> Result<PWStatusBytes, Error> {
        let psb = self.0.find(Tags::PWStatusBytes);

        if let Some(psb) = psb {
            let pws = (&psb.serialize()[..]).try_into()?;

            log::trace!("PW Status: {:x?}", pws);

            Ok(pws)
        } else {
            Err(Error::NotFound(
                "Failed to get PW status Bytes.".to_string(),
            ))
        }
    }

    /// Fingerprint, per key type.
    /// Zero bytes indicate a not defined private key.
    pub fn fingerprints(&self) -> Result<KeySet<Fingerprint>, Error> {
        let fp = self.0.find(Tags::Fingerprints);

        if let Some(fp) = fp {
            let fp: KeySet<Fingerprint> = (&fp.serialize()[..]).try_into()?;

            log::trace!("Fp: {:x?}", fp);

            Ok(fp)
        } else {
            Err(Error::NotFound("Failed to get fingerprints.".into()))
        }
    }

    pub fn ca_fingerprints(&self) -> Result<[Option<Fingerprint>; 3], Error> {
        let fp = self.0.find(Tags::CaFingerprints);

        if let Some(fp) = fp {
            // FIXME: using a KeySet is a weird hack
            let fp: KeySet<Fingerprint> = (&fp.serialize()[..]).try_into()?;

            let fp = [fp.signature, fp.decryption, fp.authentication];

            log::trace!("CA Fp: {:x?}", fp);

            Ok(fp)
        } else {
            Err(Error::NotFound("Failed to get CA fingerprints.".into()))
        }
    }

    /// Generation dates/times of key pairs
    pub fn key_generation_times(&self) -> Result<KeySet<KeyGenerationTime>, Error> {
        let kg = self.0.find(Tags::GenerationTimes);

        if let Some(kg) = kg {
            let kg: KeySet<KeyGenerationTime> = (&kg.serialize()[..]).try_into()?;

            log::trace!("Key generation: {:x?}", kg);

            Ok(kg)
        } else {
            Err(Error::NotFound(
                "Failed to get key generation times.".to_string(),
            ))
        }
    }

    pub fn key_information(&self) -> Result<Option<KeyInformation>, Error> {
        let ki = self.0.find(Tags::KeyInformation);

        // TODO: return an error in .into(), if the format of the value is bad

        Ok(ki.map(|v| v.serialize().into()))
    }

    pub fn uif_pso_cds(&self) -> Result<Option<UIF>, Error> {
        let uif = self.0.find(Tags::UifSig);

        match uif {
            None => Ok(None),
            Some(v) => Ok(Some(v.serialize().try_into()?)),
        }
    }

    pub fn uif_pso_dec(&self) -> Result<Option<UIF>, Error> {
        let uif = self.0.find(Tags::UifDec);

        match uif {
            None => Ok(None),
            Some(v) => Ok(Some(v.serialize().try_into()?)),
        }
    }

    pub fn uif_pso_aut(&self) -> Result<Option<UIF>, Error> {
        let uif = self.0.find(Tags::UifAuth);

        match uif {
            None => Ok(None),
            Some(v) => Ok(Some(v.serialize().try_into()?)),
        }
    }

    /// Get Attestation key fingerprint.
    pub fn attestation_key_fingerprint(&self) -> Result<Option<Fingerprint>, Error> {
        match self.0.find(Tags::FingerprintAttestation) {
            None => Ok(None),
            Some(data) => {
                // FIXME: move conversion logic to Fingerprint
                if data.serialize().iter().any(|&b| b != 0) {
                    Ok(Some(Fingerprint::try_from(data.serialize().as_slice())?))
                } else {
                    Ok(None)
                }
            }
        }
    }

    /// Get Attestation key algorithm attributes.
    pub fn attestation_key_algorithm_attributes(&mut self) -> Result<Option<Algo>, Error> {
        match self.0.find(Tags::AlgorithmAttributesAttestation) {
            None => Ok(None),
            Some(data) => Ok(Some(Algo::try_from(data.serialize().as_slice())?)),
        }
    }

    /// Get Attestation key generation time.
    pub fn attestation_key_generation_time(&mut self) -> Result<Option<KeyGenerationTime>, Error> {
        match self.0.find(Tags::GenerationTimeAttestation) {
            None => Ok(None),
            Some(data) => {
                // FIXME: move conversion logic to KeyGenerationTime

                // Generation time of key, binary. 4 bytes, Big Endian.
                // Value shall be seconds since Jan 1, 1970. Default value is 00000000 (not specified).
                assert_eq!(data.serialize().len(), 4);
                match u32::from_be_bytes(data.serialize().try_into().unwrap()) {
                    0 => Ok(None),
                    kgt => Ok(Some(kgt.into())),
                }
            }
        }
    }

    pub fn uif_attestation(&self) -> Result<Option<UIF>, Error> {
        let uif = self.0.find(Tags::UifAttestation);

        match uif {
            None => Ok(None),
            Some(v) => Ok(Some(v.serialize().try_into()?)),
        }
    }
}

/// Security support template (see spec pg. 24)
#[derive(Debug)]
pub struct SecuritySupportTemplate {
    // Digital signature counter [3 bytes]
    // (counts usage of Compute Digital Signature command)
    pub(crate) dsc: u32,
}

impl SecuritySupportTemplate {
    pub fn signature_count(&self) -> u32 {
        self.dsc
    }
}

/// An OpenPGP key generation Time (see spec pg. 24)
#[derive(Clone, Copy, Eq, PartialEq, Debug)]
pub struct KeyGenerationTime(u32);

impl KeyGenerationTime {
    pub fn get(&self) -> u32 {
        self.0
    }

    pub fn to_datetime(&self) -> DateTime<Utc> {
        let d = UNIX_EPOCH + Duration::from_secs(self.get() as u64);
        DateTime::<Utc>::from(d)
    }
}

impl Display for KeyGenerationTime {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.to_datetime())
    }
}

/// User Interaction Flag (UIF) (see spec pg. 24)
#[derive(Clone, Copy, Eq, PartialEq, Debug)]
pub struct UIF([u8; 2]);

impl TryFrom<Vec<u8>> for UIF {
    type Error = Error;

    fn try_from(v: Vec<u8>) -> Result<Self, Self::Error> {
        if v.len() == 2 {
            Ok(UIF(v.try_into().unwrap()))
        } else {
            Err(Error::ParseError(format!("Can't get UID from {:x?}", v)))
        }
    }
}

impl UIF {
    pub fn touch_policy(&self) -> TouchPolicy {
        self.0[0].into()
    }

    pub fn set_touch_policy(&mut self, tm: TouchPolicy) {
        self.0[0] = tm.into();
    }

    pub fn features(&self) -> Features {
        self.0[1].into()
    }

    pub(crate) fn as_bytes(&self) -> &[u8] {
        &self.0[..]
    }
}

impl Display for UIF {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "Touch policy: {} [Features: {}]",
            self.touch_policy(),
            self.features()
        )
    }
}

/// User interaction setting: is a 'touch' needed to perform an operation on the card?
/// This setting is used in 4.4.3.6 User Interaction Flag (UIF)
///
/// See spec pg 24 and <https://github.com/Yubico/yubikey-manager/blob/main/ykman/openpgp.py>
///
/// Touch policies were introduced in YubiKey Version 4.2.0 with modes ON, OFF and FIXED.
/// YubiKey Version >= 5.2.1 added support for modes CACHED and CACHED_FIXED.
#[derive(Debug, Eq, PartialEq, Clone, Copy)]
#[non_exhaustive]
pub enum TouchPolicy {
    Off,
    On,
    Fixed,
    Cached,
    CachedFixed,
    Unknown(u8),
}

impl TouchPolicy {
    /// Returns "true" if this TouchPolicy (probably) requires touch confirmation.
    ///
    /// Note: When the Policy is set to `Cached` or `CachedFixed`, there is no way to be sure if a
    /// previous touch confirmation is still valid (touch confirmations are valid for 15s, in
    /// Cached mode)
    pub fn touch_required(&self) -> bool {
        !matches!(self, Self::Off)
    }
}

impl Display for TouchPolicy {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match self {
            TouchPolicy::Off => write!(f, "Off"),
            TouchPolicy::On => write!(f, "On"),
            TouchPolicy::Fixed => write!(f, "Fixed"),
            TouchPolicy::Cached => write!(f, "Cached"),
            TouchPolicy::CachedFixed => write!(f, "CachedFixed"),
            TouchPolicy::Unknown(i) => write!(f, "Unknown({})", i),
        }
    }
}

impl From<TouchPolicy> for u8 {
    fn from(tm: TouchPolicy) -> Self {
        match tm {
            TouchPolicy::Off => 0,
            TouchPolicy::On => 1,
            TouchPolicy::Fixed => 2,
            TouchPolicy::Cached => 3,
            TouchPolicy::CachedFixed => 4,
            TouchPolicy::Unknown(i) => i,
        }
    }
}

impl From<u8> for TouchPolicy {
    fn from(i: u8) -> Self {
        match i {
            0 => TouchPolicy::Off,
            1 => TouchPolicy::On,
            2 => TouchPolicy::Fixed,
            3 => TouchPolicy::Cached,
            4 => TouchPolicy::CachedFixed,
            _ => TouchPolicy::Unknown(i),
        }
    }
}

/// "additional hardware for user interaction" (see spec 4.1.3.2)
pub struct Features(u8);

impl From<u8> for Features {
    fn from(i: u8) -> Self {
        Features(i)
    }
}

impl Display for Features {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        let mut ft = vec![];

        if self.0 & 0x80 != 0 {
            ft.push("Display")
        }
        if self.0 & 0x40 != 0 {
            ft.push("Biometric input sensor")
        }
        if self.0 & 0x20 != 0 {
            ft.push("Button")
        }
        if self.0 & 0x10 != 0 {
            ft.push("Keypad")
        }
        if self.0 & 0x8 != 0 {
            ft.push("LED")
        }
        if self.0 & 0x4 != 0 {
            ft.push("Loudspeaker")
        }
        if self.0 & 0x2 != 0 {
            ft.push("Microphone")
        }
        if self.0 & 0x1 != 0 {
            ft.push("Touchscreen")
        }

        write!(f, "{}", ft.join(", "))
    }
}

/// 4.4.3.8 Key Information
pub struct KeyInformation(Vec<u8>);

impl From<Vec<u8>> for KeyInformation {
    fn from(v: Vec<u8>) -> Self {
        KeyInformation(v)
    }
}

impl KeyInformation {
    /// How many "additional" keys do we have information for?
    pub fn num_additional(&self) -> usize {
        (self.0.len() - 6) / 2
    }

    fn get_ref(&self, n: usize) -> u8 {
        self.0[n * 2]
    }
    fn get_status(&self, n: usize) -> KeyStatus {
        self.0[n * 2 + 1].into()
    }

    pub fn sig_ref(&self) -> u8 {
        self.get_ref(0)
    }
    pub fn sig_status(&self) -> KeyStatus {
        self.get_status(0)
    }

    pub fn dec_ref(&self) -> u8 {
        self.get_ref(1)
    }
    pub fn dec_status(&self) -> KeyStatus {
        self.get_status(1)
    }

    pub fn aut_ref(&self) -> u8 {
        self.get_ref(2)
    }
    pub fn aut_status(&self) -> KeyStatus {
        self.get_status(2)
    }

    pub fn additional_ref(&self, num: usize) -> u8 {
        self.get_ref(3 + num)
    }
    pub fn additional_status(&self, num: usize) -> KeyStatus {
        self.get_status(3 + num)
    }
}

impl Display for KeyInformation {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        writeln!(
            f,
            "signature key      (#{}): {}",
            self.sig_ref(),
            self.sig_status()
        )?;
        writeln!(
            f,
            "decryption key     (#{}): {}",
            self.dec_ref(),
            self.dec_status()
        )?;
        writeln!(
            f,
            "authentication key (#{}): {}",
            self.aut_ref(),
            self.aut_status()
        )?;

        for i in 0..self.num_additional() {
            writeln!(
                f,
                "additional key {}   (#{}): {}",
                i,
                self.additional_ref(i),
                self.additional_status(i)
            )?;
        }

        Ok(())
    }
}

/// KeyStatus is contained in `KeyInformation`. It encodes if key material on a card was imported
/// or generated on the card.
#[derive(Debug, PartialEq, Eq, Clone, Copy)]
#[non_exhaustive]
pub enum KeyStatus {
    NotPresent,
    Generated,
    Imported,
    Unknown(u8),
}

impl From<u8> for KeyStatus {
    fn from(i: u8) -> Self {
        match i {
            0 => KeyStatus::NotPresent,
            1 => KeyStatus::Generated,
            2 => KeyStatus::Imported,
            _ => KeyStatus::Unknown(i),
        }
    }
}

impl Display for KeyStatus {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match self {
            KeyStatus::NotPresent => write!(f, "not present"),
            KeyStatus::Generated => write!(f, "generated"),
            KeyStatus::Imported => write!(f, "imported"),
            KeyStatus::Unknown(i) => write!(f, "unknown status ({})", i),
        }
    }
}

/// 4.2.1 Application Identifier (AID)
#[derive(Debug, Eq, PartialEq)]
pub struct ApplicationIdentifier {
    application: u8,
    version: u16,
    manufacturer: u16,
    serial: u32,
}

impl Display for ApplicationIdentifier {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "D276000124 01 {:02X} {:04X} {:04X} {:08X} 0000",
            self.application, self.version, self.manufacturer, self.serial
        )
    }
}

/// 6 Historical Bytes
#[derive(Debug, PartialEq, Eq)]
pub struct HistoricalBytes {
    /// category indicator byte
    cib: u8,

    /// Card service data (31)
    csd: Option<CardServiceData>,

    /// Card Capabilities (73)
    cc: Option<CardCapabilities>,

    /// status indicator byte (o-card 3.4.1, pg 44)
    sib: u8,
}

/// Card Capabilities (see 6 Historical Bytes)
#[derive(Debug, PartialEq, Eq)]
pub struct CardCapabilities {
    command_chaining: bool,
    extended_lc_le: bool,
    extended_length_information: bool,
}

impl Display for CardCapabilities {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        if self.command_chaining {
            writeln!(f, "- command chaining")?;
        }
        if self.extended_lc_le {
            writeln!(f, "- extended Lc and Le fields")?;
        }
        if self.extended_length_information {
            writeln!(f, "- extended Length Information")?;
        }

        Ok(())
    }
}

/// Card service data (see 6 Historical Bytes)
#[derive(Debug, PartialEq, Eq)]
pub struct CardServiceData {
    select_by_full_df_name: bool, // Application Selection by full DF name (AID)
    select_by_partial_df_name: bool, // Application Selection by partial DF name
    dos_available_in_ef_dir: bool,
    dos_available_in_ef_atr_info: bool, // should be true if extended length supported
    access_services: [bool; 3],         // should be '010' if extended length supported
    mf: bool,
}

impl Display for CardServiceData {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        if self.select_by_full_df_name {
            writeln!(f, "- Application Selection by full DF name")?;
        }
        if self.select_by_partial_df_name {
            writeln!(f, "- Application Selection by partial DF name")?;
        }
        if self.dos_available_in_ef_dir {
            writeln!(f, "- DOs available in EF.DIR")?;
        }
        if self.dos_available_in_ef_atr_info {
            writeln!(f, "- DOs available in EF.ATR/INFO")?;
        }

        write!(
            f,
            "- EF.DIR and EF.ATR/INFO access services by the GET DATA command (BER-TLV): "
        )?;
        for a in self.access_services {
            if a {
                write!(f, "1")?;
            } else {
                write!(f, "0")?;
            }
        }
        writeln!(f)?;

        if self.mf {
            writeln!(f, "- Card with MF")?;
        }

        Ok(())
    }
}

/// 4.4.3.7 Extended Capabilities
#[derive(Debug, Eq, PartialEq)]
pub struct ExtendedCapabilities {
    secure_messaging: bool,
    get_challenge: bool,
    key_import: bool,
    pw_status_change: bool,
    private_use_dos: bool,
    algo_attrs_changeable: bool,
    aes: bool,
    kdf_do: bool,

    sm_algo: u8,
    max_len_challenge: u16,
    max_len_cardholder_cert: u16,

    max_cmd_len: Option<u16>,  // v2
    max_resp_len: Option<u16>, // v2

    max_len_special_do: Option<u16>,          // v3
    pin_block_2_format_support: Option<bool>, // v3
    mse_command_support: Option<bool>,        // v3
}

impl Display for ExtendedCapabilities {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        if self.secure_messaging {
            writeln!(f, "- secure messaging")?;
        }
        if self.get_challenge {
            writeln!(f, "- get challenge")?;
        }
        if self.key_import {
            writeln!(f, "- key import")?;
        }
        if self.pw_status_change {
            writeln!(f, "- PW Status changeable")?;
        }
        if self.private_use_dos {
            writeln!(f, "- private use DOs")?;
        }
        if self.algo_attrs_changeable {
            writeln!(f, "- algorithm attributes changeable")?;
        }
        if self.aes {
            writeln!(f, "- PSO:DEC/ENC with AES")?;
        }
        if self.kdf_do {
            writeln!(f, "- KDF-DO")?;
        }
        if self.sm_algo != 0 {
            writeln!(f, "- secure messaging algorithm: {:#02X}", self.sm_algo)?;
        }

        if self.max_len_challenge != 0 {
            writeln!(
                f,
                "- maximum length of challenge: {}",
                self.max_len_challenge
            )?;
        }
        writeln!(
            f,
            "- maximum length cardholder certificates: {}",
            self.max_len_cardholder_cert
        )?;

        // v2
        if let Some(max_cmd_len) = self.max_cmd_len {
            writeln!(f, "- maximum command length: {}", max_cmd_len)?;
        }
        if let Some(max_resp_len) = self.max_resp_len {
            writeln!(f, "- maximum response length: {}", max_resp_len)?;
        }

        // v3
        if let Some(max_len_special_do) = self.max_len_special_do {
            writeln!(
                f,
                "- maximum length for special DOs: {}",
                max_len_special_do
            )?;
        }
        if self.pin_block_2_format_support == Some(true) {
            writeln!(f, "- PIN block 2 format supported")?;
        }
        if self.mse_command_support == Some(true) {
            writeln!(f, "- MSE command (for DEC and AUT) supported")?;
        }

        Ok(())
    }
}

/// 4.1.3.1 Extended length information
#[derive(Debug, Eq, PartialEq)]
pub struct ExtendedLengthInfo {
    max_command_bytes: u16,
    max_response_bytes: u16,
}

impl Display for ExtendedLengthInfo {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        writeln!(f, "- max command length: {}", self.max_command_bytes)?;
        writeln!(f, "- max response length: {}", self.max_response_bytes)?;
        Ok(())
    }
}

/// Cardholder Related Data (see spec pg. 22)
#[derive(Debug, PartialEq, Eq)]
pub struct CardholderRelatedData {
    name: Option<Vec<u8>>,
    lang: Option<Vec<Lang>>,
    sex: Option<Sex>,
}

impl Display for CardholderRelatedData {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        if let Some(name) = &self.name {
            writeln!(f, "Name: {}", Self::latin1_to_string(name))?;
        }
        if let Some(sex) = self.sex {
            writeln!(f, "Sex: {}", sex)?;
        }
        if let Some(lang) = &self.lang {
            for (n, l) in lang.iter().enumerate() {
                writeln!(f, "Lang {}: {}", n + 1, l)?;
            }
        }
        Ok(())
    }
}

/// 4.4.3.5 Sex
///
/// Encoded in accordance with <https://en.wikipedia.org/wiki/ISO/IEC_5218>
#[derive(Debug, PartialEq, Eq, Clone, Copy)]
pub enum Sex {
    NotKnown,
    Male,
    Female,
    NotApplicable,
    UndefinedValue(u8), // ISO 5218 doesn't define this value
}

impl Display for Sex {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::NotKnown => write!(f, "Not known"),
            Self::Male => write!(f, "Male"),
            Self::Female => write!(f, "Female"),
            Self::NotApplicable => write!(f, "Not applicable"),
            Self::UndefinedValue(v) => write!(f, "Undefined value {:x?}", v),
        }
    }
}

impl From<&Sex> for u8 {
    fn from(sex: &Sex) -> u8 {
        match sex {
            Sex::NotKnown => 0x30,
            Sex::Male => 0x31,
            Sex::Female => 0x32,
            Sex::NotApplicable => 0x39,
            Sex::UndefinedValue(v) => *v,
        }
    }
}

impl From<u8> for Sex {
    fn from(s: u8) -> Self {
        match s {
            0x30 => Self::NotKnown,
            0x31 => Self::Male,
            0x32 => Self::Female,
            0x39 => Self::NotApplicable,
            v => Self::UndefinedValue(v),
        }
    }
}

/// Individual language for Language Preferences (4.4.3.4), accessible via `CardholderRelatedData`.
///
/// Encoded according to <https://en.wikipedia.org/wiki/ISO_639-1>
#[derive(Debug, PartialEq, Eq, Clone, Copy)]
pub enum Lang {
    Value([u8; 2]),
    Invalid(u8),
}

impl Display for Lang {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::Value(v) => {
                write!(f, "{}{}", v[0] as char, v[1] as char)
            }
            Self::Invalid(v) => {
                write!(f, "{:x?}", v)
            }
        }
    }
}

impl From<(char, char)> for Lang {
    fn from(c: (char, char)) -> Self {
        Lang::Value([c.0 as u8, c.1 as u8])
    }
}

impl From<[char; 2]> for Lang {
    fn from(c: [char; 2]) -> Self {
        Lang::Value([c[0] as u8, c[1] as u8])
    }
}

impl From<Lang> for Vec<u8> {
    fn from(lang: Lang) -> Self {
        match lang {
            Lang::Value(v) => vec![v[0], v[1]],
            Lang::Invalid(v) => vec![v],
        }
    }
}

impl From<&[u8; 1]> for Lang {
    fn from(data: &[u8; 1]) -> Self {
        Lang::Invalid(data[0])
    }
}

impl From<&[u8; 2]> for Lang {
    fn from(data: &[u8; 2]) -> Self {
        Lang::Value([data[0], data[1]])
    }
}

/// PW status Bytes (see spec page 23)
#[derive(Debug, PartialEq, Eq)]
pub struct PWStatusBytes {
    pub(crate) pw1_cds_valid_once: bool,
    pub(crate) pw1_pin_block: bool,
    pub(crate) pw1_len_format: u8,
    pub(crate) rc_len: u8,
    pub(crate) pw3_pin_block: bool,
    pub(crate) pw3_len_format: u8,
    pub(crate) err_count_pw1: u8,
    pub(crate) err_count_rst: u8,
    pub(crate) err_count_pw3: u8,
}

impl PWStatusBytes {
    /// Set format of PW1:
    /// `false` for UTF-8 or derived password,
    /// `true` for PIN block format 2.
    pub fn set_pw1_pin_block(&mut self, val: bool) {
        self.pw1_pin_block = val;
    }

    /// Set format of PW3:
    /// `false` for UTF-8 or derived password,
    /// `true` for PIN block format 2.
    pub fn set_pw3_pin_block(&mut self, val: bool) {
        self.pw3_pin_block = val;
    }

    /// Is PW1 (no. 81) only valid for one PSO:CDS command?
    pub fn pw1_cds_valid_once(&self) -> bool {
        self.pw1_cds_valid_once
    }

    /// Configure if PW1 (no. 81) is only valid for one PSO:CDS command.
    pub fn set_pw1_cds_valid_once(&mut self, val: bool) {
        self.pw1_cds_valid_once = val;
    }

    /// Max length of PW1
    pub fn pw1_max_len(&self) -> u8 {
        self.pw1_len_format & 0x7f
    }

    /// Max length of Resetting Code (RC) for PW1
    pub fn rc_max_len(&self) -> u8 {
        self.rc_len
    }

    /// Max length of PW3
    pub fn pw3_max_len(&self) -> u8 {
        self.pw3_len_format & 0x7f
    }

    /// Error counter of PW1 (if 0, then PW1 is blocked).
    pub fn err_count_pw1(&self) -> u8 {
        self.err_count_pw1
    }

    /// Error counter of Resetting Code (RC) (if 0, then RC is blocked).
    pub fn err_count_rc(&self) -> u8 {
        self.err_count_rst
    }

    /// Error counter of PW3 (if 0, then PW3 is blocked).
    pub fn err_count_pw3(&self) -> u8 {
        self.err_count_pw3
    }
}

/// Fingerprint (see spec pg. 23)
#[derive(Clone, Eq, PartialEq)]
pub struct Fingerprint([u8; 20]);

impl Fingerprint {
    pub fn to_spaced_hex(&self) -> String {
        let mut fp = String::new();

        for i in 0..20 {
            let _ = write!(&mut fp, "{:02X}", self.0[i]);

            if i < 19 && (i % 2 == 1) {
                fp.push(' ');
            }
            if i == 9 {
                fp.push(' ');
            }
        }

        fp
    }
}

/// Helper fn for nom parsing
pub(crate) fn complete<O>(result: nom::IResult<&[u8], O>) -> Result<O, Error> {
    let (rem, output) = result.map_err(|_err| Error::ParseError("Parsing failed".to_string()))?;
    if rem.is_empty() {
        Ok(output)
    } else {
        Err(Error::ParseError(format!(
            "Parsing incomplete, trailing data: {:x?}",
            rem
        )))
    }
}
