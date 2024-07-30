//cargo-deps: json="0.12.4"

// Script takes arguments and transforms them into dict with arrays as dict values
// and returns as JSON
use std::env;
use json::JsonValue;

extern crate json;
fn main() {
    let args: Vec<String> = env::args().skip(1).collect();

    let input_string = args.join(" ");
    let substrings: Vec<&str> = input_string.split_whitespace().collect();

    let mut json_object = JsonValue::new_object();

    for substring in substrings {
        let letters_array: Vec<JsonValue> = substring.to_uppercase()
            .chars()
            .map(|c| JsonValue::String(c.to_string()))
            .collect();

        json_object[substring] = JsonValue::Array(letters_array);
    }

    println!("{}", json_object.pretty(2));
}
