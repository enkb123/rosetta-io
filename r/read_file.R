file_path <- commandArgs(trailingOnly = TRUE)[1]

con <- file(file_path, "r")

i <- 1
while (length(line <- readLines(con, n = 1)) > 0) {
  cat(i, toupper(line), sep = " ", fill = TRUE)
  i <- i + 1
}

close(con)
