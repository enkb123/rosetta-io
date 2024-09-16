library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

string_lengths <- sapply(args, nchar)

cat(toJSON(string_lengths))
