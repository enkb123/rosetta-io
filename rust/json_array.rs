//cargo-deps: json="0.12.4"

use std::env;
use json::JsonValue;

extern crate json;

fn main() {
    let args: Vec<String> = env::args().collect();

    let input_string = args[1..].join(" ");

    let substrings: Vec<&str> = input_string.split_whitespace().collect();

    let mut json_array = JsonValue::new_array();

    for substring in substrings {
        let escaped = substring.replace('"', "\\\"");
        json_array.push(escaped).expect("Failed to add element to JSON array");
    }

    println!("{}", json_array.pretty(2)); // Pretty-print with an indentation of 2 spaces
}
