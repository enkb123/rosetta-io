args <- commandArgs(trailingOnly = TRUE)
outfile <- args[1]
text <- args[2]

writeLines(toupper(text), outfile, sep="")
