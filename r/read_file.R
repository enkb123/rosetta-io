file_path <- "./my-text-file.txt"

lines <- readLines(file_path)

for (line in lines) {
  cat("line:", line, "\n")
}
