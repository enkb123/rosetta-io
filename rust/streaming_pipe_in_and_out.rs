use std::fs::File;
use std::io::{self, BufRead, Write};
use std::path::Path;

fn main() -> io::Result<()> {
    let input_path = "streaming-in.pipe";
    let output_path = "streaming-out.pipe";

    let mut output = File::create(output_path)?;

    let input = File::open(input_path)?;
    let reader = io::BufReader::new(input);

    for line in reader.lines() {
        let line = line?;
        writeln!(output, "received {}", line)?;
    }

    Ok(())
}
