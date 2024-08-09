//Script reads text from a named pipe and writes it to stdout, capitalized

use std::env;
use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn main() {
    let args: Vec<String> = env::args().collect();

    let pipe_in = &args[1];

    let file = File::open(pipe_in).unwrap();
    let reader = BufReader::new(file);

    for line in reader.lines() {
        println!("{}", line.unwrap().to_uppercase());
    }

}
