// SPDX-FileCopyrightText: 2021 Heiko Schaefer <heiko@schaefer.name>
// SPDX-License-Identifier: MIT OR Apache-2.0

//! Data structure for APDU Commands
//! (Commands get sent to the card, which will usually send back a `Response`)

#[derive(Clone, Copy)]
pub enum Expect {
    Empty,
    Some,
    Short(u8),
}

#[derive(Clone, Debug)]
pub(crate) struct Command {
    // Class byte (CLA)
    cla: u8,

    // Instruction byte (INS)
    ins: u8,

    // Parameter bytes (P1/P2)
    p1: u8,
    p2: u8,

    // NOTE: data must be smaller than 64 kbyte
    data: Vec<u8>,
}

impl Command {
    /// Create an APDU Command.
    ///
    /// `data` must be smaller than 64 kbyte. If a larger `data` is passed,
    /// this fn will panic.
    pub fn new(cla: u8, ins: u8, p1: u8, p2: u8, data: Vec<u8>) -> Self {
        // This constructor is the only place `data` gets set, so it's
        // sufficient to check it here.
        if data.len() > u16::MAX as usize {
            panic!("'data' too big, must be <64 kbyte");
        }

        Command {
            cla,
            ins,
            p1,
            p2,
            data,
        }
    }

    pub(crate) fn ins(&self) -> u8 {
        self.ins
    }

    pub(crate) fn p1(&self) -> u8 {
        self.p1
    }

    pub(crate) fn p2(&self) -> u8 {
        self.p2
    }

    pub(crate) fn data(&self) -> &[u8] {
        &self.data
    }

    /// Serialize a Command (for sending to a card).
    ///
    /// See OpenPGP card spec, chapter 7 (pg 47)
    pub(crate) fn serialize(
        &self,
        ext_len: bool,
        expect_response: Expect,
    ) -> Result<Vec<u8>, crate::Error> {
        // FIXME? (from scd/apdu.c):
        //  T=0 does not allow the use of Lc together with Le;
        //  thus disable Le in this case.

        // "number of bytes in the command data field"
        assert!(self.data.len() <= u16::MAX as usize);
        let nc = self.data.len() as u16;

        let mut buf = vec![self.cla, self.ins, self.p1, self.p2];
        buf.extend(Self::make_lc(nc, ext_len));
        buf.extend(&self.data);
        buf.extend(Self::make_le(nc, ext_len, expect_response));

        Ok(buf)
    }

    /// Encode len for Lc field
    fn make_lc(len: u16, ext_len: bool) -> Vec<u8> {
        if !ext_len {
            assert!(
                len <= 0xff,
                "unexpected: len = {:x?}, but ext says Short",
                len
            );
        }

        if len == 0 {
            vec![]
        } else if !ext_len {
            vec![len as u8]
        } else {
            vec![0, (len >> 8) as u8, (len & 255) as u8]
        }
    }

    /// Encode value for Le field
    /// ("maximum number of bytes expected in the response data field").
    fn make_le(nc: u16, ext_len: bool, expect_response: Expect) -> Vec<u8> {
        match (ext_len, expect_response) {
            (_, Expect::Empty) => {
                // No response data expected.
                // "If the Le field is absent, then Ne is zero"
                vec![]
            }
            (false, Expect::Some) => {
                // A short Le field consists of one byte with any value
                vec![0]
            }
            (false, Expect::Short(size)) => {
                // A short Le field consists of one byte with any value
                vec![size]
            }
            (true, Expect::Some) => {
                if nc == 0 {
                    // "three bytes (one byte set to '00' followed by two
                    // bytes with any value) if the Lc field is absent"
                    vec![0, 0, 0]
                } else {
                    // "two bytes (with any value) if an extended Lc field
                    // is present"
                    vec![0, 0]
                }
            }
            _ => {
                unreachable!("This should not happen")
            }
        }
    }
}
