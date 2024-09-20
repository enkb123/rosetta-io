file_path <- "./my-text-file.txt"

con <- file(file_path, "r")

while (length(line <- readLines(con, n = 1, warn = FALSE)) > 0) {
  cat("line:", line, "\n")
}

close(con)
