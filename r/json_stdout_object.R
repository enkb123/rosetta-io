library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

string_length <- list()
for (string in args) {
  string_length[[string]] <- nchar(string)
}

cat(toJSON(string_length, auto_unbox = TRUE))
