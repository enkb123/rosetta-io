text_raw <- charToRaw("Hello World ")
null_char_raw <- as.raw(0)
new_line_raw <- charToRaw("\n")
raw_vector <- c(text_raw, null_char_raw, new_line_raw)

writeBin(raw_vector, "temp_binary_file.bin")

system("cat temp_binary_file.bin", intern = FALSE)

unlink("temp_binary_file.bin")
