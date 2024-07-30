//cargo-deps: base64="0.13"

use std::env;
extern crate base64;

fn main() {
    let args: Vec<String> = env::args().collect();

    let test_string = &args[1];

    let encoded_string = base64::encode(test_string);

    println!("{}", encoded_string);
}
