i <- 1
for (line in readLines("stdin")) {
  cat(i, toupper(line), sep = " ", fill = TRUE)
  i <- i + 1
}
