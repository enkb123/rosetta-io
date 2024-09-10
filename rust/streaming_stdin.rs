use std::io::{self, BufRead, Write};

fn main() {
    let mut stdout_handle = io::stdout().lock();
    let stdin_handle = io::stdin().lock();

    for line in stdin_handle.lines() {
        writeln!(stdout_handle, "{}", line.unwrap().to_uppercase()).unwrap();
        stdout_handle.flush().unwrap();
    }
}
