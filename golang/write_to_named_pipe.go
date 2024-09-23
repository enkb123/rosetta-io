package main

import (
	"os"
	"syscall"
)

func main() {
	pipePath := "output.pipe"

	syscall.Mkfifo(pipePath, 0666)

	file, _ := os.OpenFile(pipePath, os.O_WRONLY|os.O_APPEND, os.ModeNamedPipe)
	defer file.Close()

	file.WriteString("Hello World!")
}
