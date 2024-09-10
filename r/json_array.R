library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

cat(toJSON(args))
