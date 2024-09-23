package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	pipeIn := "input.pipe"

	file, _ := os.Open(pipeIn)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		fmt.Println(strings.ToUpper(line))
	}
}
