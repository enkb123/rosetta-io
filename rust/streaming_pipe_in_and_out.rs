use std::fs::File;
use std::io::{self, BufRead, BufReader, Write};

fn main() {
    let mut output = File::create("streaming-out.pipe").unwrap();
    let input = File::open("streaming-in.pipe").unwrap();

    for line in BufReader::new(input).lines() {
        writeln!(output, "received {}", line.unwrap()).unwrap();
    }
}
