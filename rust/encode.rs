//cargo-deps: base64="0.13"

use std::env;
extern crate base64;

fn main() {
    let test_string = env::args().nth(1).unwrap();
    let encoded_string = base64::encode(test_string);

    println!("{}", encoded_string);
}
