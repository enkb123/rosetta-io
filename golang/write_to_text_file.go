package main

import (
	"os"
)

func main() {
	os.WriteFile("output.txt", []byte("Hello World!"), 0)
}
