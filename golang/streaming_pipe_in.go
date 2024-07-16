//Script reads text from a named pipe and writes it to stdout, capitalized

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	pipeIn := os.Args[1]

	file, _ := os.Open(pipeIn)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		fmt.Println(strings.ToUpper(line))
	}
}
