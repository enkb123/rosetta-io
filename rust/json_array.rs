//cargo-deps: json="0.12.4"

use json::JsonValue;
use std::env;
extern crate json;

fn main() {
    let args: Vec<String> = env::args().collect();

    let substrings: Vec<String> = args[1..]
        .iter()
        .flat_map(|arg| arg.split_whitespace())
        .map(|s| s.to_string())
        .collect();

    let json_array: JsonValue = substrings.into();
    println!("{}", json_array);
}
