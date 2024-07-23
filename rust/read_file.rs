use std::env;
use std::fs::File;
use std::io::{self, BufRead};

fn main() -> Result<(), io::Error> {
    // Read command-line arguments
    let args: Vec<String> = env::args().collect();

    // Check if filename argument is provided
    if args.len() < 2 {
        eprintln!("Usage: {} <filename>", args[0]);
        std::process::exit(1);
    }
    let filename = &args[1];

    // Open the file
    let file = File::open(filename)?;
    let reader = io::BufReader::new(file);

    // Initialize line number counter
    let mut line_number = 1;

    // Read and print each line capitalized and numbered
    for line in reader.lines() {
        let line = line?;
        println!("{} {}", line_number, line.to_uppercase());
        line_number += 1;
    }

    Ok(())
}
