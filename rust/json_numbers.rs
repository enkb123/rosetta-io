//cargo-deps: json="0.12.4"

// Script takes string arguments and outputs a JSON array of numbers representing
// the length of each argument
use std::env;
use json::JsonValue;

extern crate json;
fn main() {
    let args: Vec<String> = env::args().collect();

    let mut json_array = JsonValue::new_array();

    for arg in args.iter().skip(1) {
        json_array.push(arg.len()).expect("Failed to push length to JSON array");
    }

    println!("{}", json_array.pretty(2));
}
