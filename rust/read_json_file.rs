//cargo-deps: json="0.12.4"

use std::env;
use std::fs;
extern crate json;
fn main() {
    let filename = env::args().nth(1).unwrap();

    let json_string = fs::read_to_string(filename).unwrap();
    let parsed_json = json::parse(&json_string).unwrap();

    let people = parsed_json.members();
    for person in people {
        let age = person["age"].as_u32().unwrap();
        let first_name = person["first_name"].as_str().unwrap();
        println!("Hello, {} year old {}", age, first_name);
    }
}
