use std::env;
use std::fs::File;
use std::io::{BufReader, BufRead};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args: Vec<String> = env::args().collect();
    let file_path = &args[1];

    let file = File::open(file_path)?;
    let reader = BufReader::new(file);

    let mut line_number = 1;

    for line_result in reader.lines() {
        let line = line_result?;
        println!("{} {}", line_number, line.to_uppercase());
        line_number += 1;
    }

    Ok(())
}
