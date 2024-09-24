//cargo-deps: json="0.12.4"
use std::fs;

extern crate json;

fn main() {
    let filename = "people.json";

    let json_string = fs::read_to_string(filename).unwrap();
    let parsed_json = json::parse(&json_string).unwrap();

    for person in parsed_json.members() {
        let age = person["age"].as_u32().unwrap();
        let first_name = person["first_name"].as_str().unwrap();
        println!("Hello, {} year old {}", age, first_name);
    }
}
