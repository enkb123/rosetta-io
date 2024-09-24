temp_file <- tempfile()

writeBin(c(charToRaw("Hello World "), as.raw(0), charToRaw("\n")), temp_file)

system(paste("cat", temp_file))

unlink(temp_file)
