args <- commandArgs(trailingOnly = TRUE)

pipe_in <- args[1]
pipe_out <- args[2]


input <- file(pipe_in, "r")

output <- file(pipe_out, "w")

while (length(line <- readLines(input, n = 1)) > 0) {
  writeLines(toupper(line), output)
  flush(output)
}

close(input)
close(output)
