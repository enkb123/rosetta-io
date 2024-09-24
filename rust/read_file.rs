use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn main() {
    let file = File::open("./my-text-file.txt").unwrap();

    for line in BufReader::new(file).lines() {
        println!("line: {}", line.unwrap());
    }
}
