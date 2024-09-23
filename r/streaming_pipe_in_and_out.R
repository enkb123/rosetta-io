input_file <- "streaming-in.pipe"
output_file <- "streaming-out.pipe"


input <- file(input_file, "r")

output <- file(output_file, "w")

while (length(line <- readLines(input, n = 1)) > 0) {
  writeLines(paste("received", line), con = output)
  flush(output)
}

close(input)
close(output)
