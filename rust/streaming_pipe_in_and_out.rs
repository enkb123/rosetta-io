// Script reads text from a named pipe and writes it another named pipe, capitalized
use std::env;
use std::fs::File;
use std::io::{self, BufRead, BufWriter, Write};

fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();

    let pipe_in = &args[1];
    let pipe_out = &args[2];

    let input_file = File::open(pipe_in)?;
    let output_file = File::create(pipe_out)?;

    let reader = io::BufReader::new(input_file);
    let mut writer = BufWriter::new(output_file);

    for line in reader.lines() {
        match line {
            Ok(line) => {
                let _ = writeln!(writer, "{}", line.to_uppercase());
                let _ = writer.flush();
            }
            Err(_) => todo!(),
        }
    }

    Ok(())
}
