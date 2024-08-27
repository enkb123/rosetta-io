//Script reads text from a named pipe and writes it to stdout, capitalized

use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let pipe_in = env::args().nth(1).unwrap();

    let file = File::open(pipe_in).unwrap();
    let reader = BufReader::new(file);

    for line in reader.lines() {
        println!("{}", line.unwrap().to_uppercase());
    }
}