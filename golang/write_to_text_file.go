package main

import (
	"os"
)

func main() {

	outFile := "output.txt"
	text := "Hello World!"

	_ = os.WriteFile(outFile, []byte(text), 0644)

}
