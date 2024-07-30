//cargo-deps: json="0.12.4"

// Script outputs arrays of objects as JSON
use std::env;
use json::JsonValue;

extern crate json;
fn main() {
    let args: Vec<String> = env::args().skip(1).collect();

    let input_string = args.join(" ");

    let substrings: Vec<&str> = input_string.split_whitespace().collect();

    let mut json_array = JsonValue::new_array();

    for substring in substrings {
        let key = substring.to_uppercase();
        let value = substring.len();

        let mut json_object = JsonValue::new_object();
        json_object[key] = JsonValue::Number(value.into());

        json_array.push(json_object).unwrap();
    }

    let json_string = json_array.dump();

    let formatted_json_string = json_string
        .replace(",", ", ")
        .replace(":", ": ");

    println!("{}", formatted_json_string);
}
