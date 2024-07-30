// Script reads streaming input text and then prints capitalized string to stdout

use std::io::{self, BufRead, Write};

fn main() {
    let stdout = io::stdout();
    let mut stdout_handle = stdout.lock();

    let stdin = io::stdin();
    let stdin_handle = stdin.lock();

    for line in stdin_handle.lines() {
        match line {
            Ok(line) => {
                writeln!(stdout_handle, "{}", line.to_uppercase()).unwrap();
                stdout_handle.flush().unwrap();
            }
            Err(_) => todo!(),

        }
    }
}
