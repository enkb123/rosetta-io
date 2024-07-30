//Script reads text from a named pipe and writes it to stdout, capitalized

use std::env;
use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();

    let pipe_in = &args[1];

    let file = File::open(pipe_in)?;
    let reader = BufReader::new(file);

    for line in reader.lines() {
        match line {
            Ok(line) => {
                println!("{}", line.to_uppercase());
            }
            Err(_) => todo!(),

        }
    }

    Ok(())
}
