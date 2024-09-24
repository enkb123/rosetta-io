while(length(line <- readLines("stdin", n = 1L)) > 0) {
  cat("received", line, "\n")
}
