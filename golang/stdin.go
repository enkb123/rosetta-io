// Test script to get input, transform, and write to stdout
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	counter := 1

	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			break
		}
		fmt.Printf("%d %s\n", counter, strings.ToUpper(line))
		counter++
	}
}
