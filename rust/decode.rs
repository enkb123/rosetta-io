//cargo-deps: base64="0.13"

//Script to decode Base64 text
extern crate base64;
use std::env;
use base64::decode;

fn main() {
    let args: Vec<String> = env::args().collect();

    let encoded_string = &args[1];

    match decode(encoded_string) {
        Ok(decoded_bytes) => {
            match String::from_utf8(decoded_bytes) {
                Ok(decoded_string) => println!("{}", decoded_string),
                Err(_) => todo!(),
            }
        }
        Err(_) => todo!(),
    }
}
