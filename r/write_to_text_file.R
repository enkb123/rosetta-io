args <- commandArgs(trailingOnly = TRUE)
outfile <- "output.txt"
text <- "Hello World!"

writeLines(text, outfile, sep="")
