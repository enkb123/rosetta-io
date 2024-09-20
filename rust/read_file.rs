use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn main() {
    let file_path = "./my-text-file.txt";
    let file = File::open(file_path).unwrap();

    let reader = BufReader::new(file);

    for line in reader.lines() {
        println!("line: {}", line.unwrap());
    }
}
