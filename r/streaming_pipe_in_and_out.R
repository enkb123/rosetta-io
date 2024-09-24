input <- file("streaming-in.pipe", "r")
output <- file("streaming-out.pipe", "w")

while (length(line <- readLines(input, n = 1)) > 0) {
  writeLines(paste("received", line), con = output)
  flush(output)
}

close(input)
close(output)
