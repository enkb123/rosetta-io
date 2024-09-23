pipe_path <- "output.pipe"

if (!file.exists(pipe_path)) {
  system(paste("mkfifo", pipe_path))
}

pipe <- file(pipe_path, open = "w")

writeLines("Hello World!", pipe)

close(pipe)
