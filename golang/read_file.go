package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	filePath := "./my-text-file.txt"

	file, _ := os.Open(filePath)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if line != "" {
			fmt.Println("line:", line)
		}
	}
}
