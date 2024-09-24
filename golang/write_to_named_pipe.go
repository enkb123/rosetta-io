package main

import (
	"os"
)

func main() {
	os.WriteFile("output.pipe", []byte("Hello World!"), 0)
}
