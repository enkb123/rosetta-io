args <- commandArgs(trailingOnly = TRUE)

pipe_in <- args[1]

input <- file(pipe_in, "r")

while (length(line <- readLines(input, n = 1)) > 0) {
  cat(paste(toupper(line), "\n", sep = ""))
}

close(input)
