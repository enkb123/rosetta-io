//cargo-deps: json="0.12.4"

use json::JsonValue;
use std::env;

extern crate json;

fn main() {
    let test_string = env::args().nth(1).expect("Expected one argument");

    let json_value: JsonValue = test_string.into();

    println!("{}", json_value.dump());
}
