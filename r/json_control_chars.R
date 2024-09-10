library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

cat(toJSON(args, auto_unbox = TRUE))
