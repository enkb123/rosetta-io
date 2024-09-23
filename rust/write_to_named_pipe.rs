use std::fs::OpenOptions;
use std::io::Write;
use std::process::Command;

fn main() {
    let pipe_path = "output.pipe";

    if std::fs::metadata(pipe_path).is_err() {
        Command::new("mkfifo")
            .arg(pipe_path)
            .status();
    }

    let mut pipe = OpenOptions::new()
        .write(true)
        .open(pipe_path)
        .expect("Could not open named pipe");

    pipe.write_all(b"Hello World!\n");
}
