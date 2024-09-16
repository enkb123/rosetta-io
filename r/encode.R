library(base64enc)

args <- commandArgs(trailingOnly = TRUE)

encoded_string <- base64encode(charToRaw(args))

cat(encoded_string)
