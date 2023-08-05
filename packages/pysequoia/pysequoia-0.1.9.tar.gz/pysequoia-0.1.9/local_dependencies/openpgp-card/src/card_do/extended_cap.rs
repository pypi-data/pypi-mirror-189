// SPDX-FileCopyrightText: 2021 Heiko Schaefer <heiko@schaefer.name>
// SPDX-License-Identifier: MIT OR Apache-2.0

//! 4.4.3.7 Extended Capabilities

use std::convert::TryFrom;

use crate::card_do::ExtendedCapabilities;
use crate::Error;

impl ExtendedCapabilities {
    pub fn max_len_special_do(&self) -> Option<u16> {
        self.max_len_special_do
    }

    pub fn algo_attrs_changeable(&self) -> bool {
        self.algo_attrs_changeable
    }

    pub fn max_cmd_len(&self) -> Option<u16> {
        self.max_cmd_len
    }

    pub fn max_resp_len(&self) -> Option<u16> {
        self.max_resp_len
    }
}

impl TryFrom<(&[u8], u16)> for ExtendedCapabilities {
    type Error = Error;

    fn try_from((input, version): (&[u8], u16)) -> Result<Self, Self::Error> {
        // FIXME: check that this fn is not called excessively often

        let version = ((version >> 8) as u8, (version & 0xff) as u8);

        // FIXME: earlier versions have shorter extended capabilities
        assert!(version.0 >= 2);

        // v2.x and v3.x should have 10 byte sized extended caps
        assert_eq!(
            input.len(),
            10,
            "extended capabilities with size != 10 are currently unsupported"
        );

        let b = input[0];

        let secure_messaging = b & 0x80 != 0;
        let get_challenge = b & 0x40 != 0;
        let key_import = b & 0x20 != 0;
        let pw_status_change = b & 0x10 != 0;
        let private_use_dos = b & 0x08 != 0;
        let algo_attrs_changeable = b & 0x04 != 0;
        let aes = b & 0x02 != 0;
        let kdf_do = b & 0x01 != 0;

        let sm_algo = input[1];

        let max_len_challenge = input[2] as u16 * 256 + input[3] as u16;
        let max_len_cardholder_cert = input[4] as u16 * 256 + input[5] as u16;

        let mut max_cmd_len = None;
        let mut max_resp_len = None;

        let mut max_len_special_do = None;
        let mut pin_block_2_format_support = None;
        let mut mse_command_support = None;

        if version.0 == 2 {
            // v2.0 until v2.2
            max_cmd_len = Some(input[6] as u16 * 256 + input[7] as u16);
            max_resp_len = Some(input[8] as u16 * 256 + input[9] as u16);
        } else {
            // from v3.0
            max_len_special_do = Some(input[6] as u16 * 256 + input[7] as u16);

            let i8 = input[8];
            let i9 = input[9];

            if i8 > 1 {
                return Err(Error::ParseError(format!(
                    "Illegal value '{}' for pin_block_2_format_support",
                    i8
                )));
            }

            pin_block_2_format_support = Some(i8 != 0);

            if i9 > 1 {
                return Err(Error::ParseError(format!(
                    "Illegal value '{}' for mse_command_support",
                    i9
                )));
            }
            mse_command_support = Some(i9 != 0);
        }

        Ok(Self {
            secure_messaging,
            get_challenge,
            key_import,
            pw_status_change,
            private_use_dos,
            algo_attrs_changeable,
            aes,
            kdf_do,

            sm_algo,
            max_len_challenge,
            max_len_cardholder_cert,

            max_cmd_len,  // v2
            max_resp_len, // v2

            max_len_special_do,         // v3
            pin_block_2_format_support, // v3
            mse_command_support,        // v3
        })
    }
}

#[cfg(test)]
mod test {
    use std::convert::TryFrom;

    use hex_literal::hex;

    use crate::card_do::extended_cap::ExtendedCapabilities;

    #[test]
    fn test_yk5() {
        // YubiKey 5
        let data = hex!("7d 00 0b fe 08 00 00 ff 00 00");

        let ec = ExtendedCapabilities::try_from((&data[..], 0x0304)).unwrap();

        assert_eq!(
            ec,
            ExtendedCapabilities {
                secure_messaging: false,
                get_challenge: true,
                key_import: true,
                pw_status_change: true,
                private_use_dos: true,
                algo_attrs_changeable: true,
                aes: false,
                kdf_do: true,
                sm_algo: 0x0,
                max_len_challenge: 0xbfe,
                max_len_cardholder_cert: 0x800,
                max_cmd_len: None,
                max_resp_len: None,
                max_len_special_do: Some(0xff),
                pin_block_2_format_support: Some(false),
                mse_command_support: Some(false),
            }
        );
    }

    #[test]
    fn test_floss21() {
        // FLOSS shop2.1
        let data = hex!("7c 00 08 00 08 00 08 00 08 00");

        let ec = ExtendedCapabilities::try_from((&data[..], 0x0201)).unwrap();

        assert_eq!(
            ec,
            ExtendedCapabilities {
                secure_messaging: false,
                get_challenge: true,
                key_import: true,
                pw_status_change: true,
                private_use_dos: true,
                algo_attrs_changeable: true,
                aes: false,
                kdf_do: false,
                sm_algo: 0,
                max_len_challenge: 2048,
                max_len_cardholder_cert: 2048,
                max_cmd_len: Some(2048),
                max_resp_len: Some(2048),
                max_len_special_do: None,
                pin_block_2_format_support: None,
                mse_command_support: None,
            }
        );
    }
}
