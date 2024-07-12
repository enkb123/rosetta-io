# Script reads text from a named pipe and writes it to stdout, capitalized
# Command-line arguments
args <- commandArgs(trailingOnly = TRUE)

# Named pipe path (input)
pipe_in <- args[1]

# Open named pipe for reading
input <- file(pipe_in, "r")

# Read each line from input pipe, convert to uppercase, and print to stdout
while (TRUE) {
  line <- readLines(input, n = 1)
  if (length(line) == 0) {
    break  # Exit loop when there's no more data to read
  }
  cat(paste(toupper(line), "\n", sep = ""))    # Print capitalized line to stdout
}

# Close input pipe
close(input)
