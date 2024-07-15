// Read a file from file path (given as a command line arg),
// print line by line with line numbers
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	content, _ := os.ReadFile(os.Args[1])

	lines := strings.Split(string(content), "\n")
	lineNumber := 1

	for _, line := range lines {
		if line == "" {
			continue
		}
		fmt.Printf("%d %s\n", lineNumber, strings.ToUpper(line))
		lineNumber++
	}
}
