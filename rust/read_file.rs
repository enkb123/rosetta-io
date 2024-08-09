use std::env;
use std::fs::File;
use std::io::{BufReader, BufRead};

fn main() {
    let args: Vec<String> = env::args().collect();
    let file_path = &args[1];

    let file = File::open(file_path).unwrap();
    let reader = BufReader::new(file);

    for (mut line_number, line_result) in reader.lines().enumerate() {
        line_number += 1;
        let line = line_result.unwrap();
        println!("{} {}", line_number, line.to_uppercase());
    }

}
