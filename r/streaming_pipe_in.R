pipe_in <- "input.pipe"

input <- file(pipe_in, "r")

while (length(line <- readLines(input, n = 1)) > 0) {
  cat(paste(toupper(line), "\n", sep = ""))
}

close(input)
