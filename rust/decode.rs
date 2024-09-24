//cargo-deps: base64="0.13"

extern crate base64;

use base64::decode;
use std::env;

fn main() {
    let encoded_string = env::args().nth(1).unwrap();
    let decoded_bytes = decode(encoded_string).unwrap();
    let decoded_string = String::from_utf8(decoded_bytes).unwrap();
    println!("{}", decoded_string);
}
