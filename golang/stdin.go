package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for lineNumber := 1; scanner.Scan(); lineNumber++ {
		fmt.Printf("%d %s\n", lineNumber, strings.ToUpper(scanner.Text()))
	}
}
