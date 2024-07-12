# Script reads text from a named pipe and writes it another named pipe, capitalized
args <- commandArgs(trailingOnly = TRUE)

pipe_in <- args[1]
pipe_out <- args[2]


input <- file(pipe_in, "r")

output <- file(pipe_out, "w")

while (TRUE) {
  line <- readLines(input, n = 1)
  if (length(line) == 0) {
    break
  }
  writeLines(toupper(line), output)
  flush(output)
}

close(input)
close(output)
