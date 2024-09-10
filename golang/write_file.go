package main

import (
	"os"
	"strings"
)

func main() {

	outFile := os.Args[1]
	text := strings.ToUpper(os.Args[2])

	_ = os.WriteFile(outFile, []byte(text), 0644)

}
