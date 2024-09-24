use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let file = File::open("input.pipe").unwrap();

    for line in BufReader::new(file).lines() {
        println!("{}", line.unwrap().to_uppercase());
    }
}
