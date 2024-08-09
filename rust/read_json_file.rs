//cargo-deps: json="0.12.4"

use std::fs;
use std::env;
use json::JsonValue;
extern crate json;
fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];

    let json_string = fs::read_to_string(filename).unwrap();
    let parsed_json = json::parse(&json_string).unwrap();

    match parsed_json {
        JsonValue::Array(people) => {
            for person in people.iter() {
                let age = person["age"].as_u32().unwrap();
                let first_name = person["first_name"].as_str().unwrap();
                println!("Hello, {} year old {}", age, first_name);
            }
        },
        _ => {}
    }
}
