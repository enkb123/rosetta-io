//cargo-deps: json="0.12.4"

use std::fs::File;
use std::io::Read;
use std::env;
use json::{parse, JsonValue};


extern crate json;

#[derive(Debug)]
struct Person {
    age: u32,
    first_name: String,
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args: Vec<String> = env::args().collect();

    let filename = &args[1];

    let mut file = File::open(filename)?;
    let mut json_string = String::new();
    file.read_to_string(&mut json_string)?;

    let parsed_json = parse(&json_string)?;

    let mut people = Vec::new();
    if let JsonValue::Array(items) = parsed_json {
        for item in items {
            let age = item["age"].as_u32().unwrap_or(0);
            let first_name = item["first_name"].as_str().unwrap_or("");
            let person = Person {
                age,
                first_name: first_name.to_string(),
            };
            people.push(person);
        }
    }

    for person in people {
        println!("Hello, {} year old {}", person.age, person.first_name);
    }

    Ok(())
}
