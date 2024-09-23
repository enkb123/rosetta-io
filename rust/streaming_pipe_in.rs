use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let pipe_in = "input.pipe";

    let file = File::open(pipe_in).unwrap();
    let reader = BufReader::new(file);

    for line in reader.lines() {
        println!("{}", line.unwrap().to_uppercase());
    }
}
