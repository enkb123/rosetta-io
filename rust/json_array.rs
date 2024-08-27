//cargo-deps: json="0.12.4"

use json::JsonValue;
use std::env;
extern crate json;

fn main() {
    let substrings: Vec<String> = env::args().skip(1).collect();
    let json_array: JsonValue = substrings.into();
    println!("{}", json_array.dump());
}
