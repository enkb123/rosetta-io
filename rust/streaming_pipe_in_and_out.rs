use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader, BufWriter, Write};

fn main() {
    let args: Vec<String> = env::args().collect();

    let pipe_in = &args[1];
    let pipe_out = &args[2];

    let reader = BufReader::new(File::open(pipe_in).unwrap());
    let mut writer = BufWriter::new(File::create(pipe_out).unwrap());

    for line in reader.lines() {
        writeln!(writer, "{}", line.unwrap().to_uppercase()).unwrap();
        writer.flush().unwrap();
    }
}
