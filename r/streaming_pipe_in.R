input <- file("input.pipe", "r")

while (length(line <- readLines(input, n = 1)) > 0) {
  cat(toupper(line), "\n")
}

close(input)
