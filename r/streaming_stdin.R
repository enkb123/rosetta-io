while(length(line <- readLines("stdin", n = 1L)) > 0) {
  cat(toupper(line), fill = TRUE)
}
