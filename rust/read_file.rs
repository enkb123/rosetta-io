use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let file_path = env::args().nth(1).unwrap();

    let file = File::open(file_path).unwrap();
    let reader = BufReader::new(file);

    for (line_number, line_result) in reader.lines().enumerate() {
        let line = line_result.unwrap();
        println!("{} {}", line_number + 1, line.to_uppercase());
    }
}
