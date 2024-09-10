library(base64enc)

args <- commandArgs(trailingOnly = TRUE)

decoded_string <- rawToChar(base64decode(args))

cat(decoded_string, fill = TRUE)
