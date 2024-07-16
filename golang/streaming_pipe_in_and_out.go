// Script reads text from a named pipe and writes it to another pipe, capitalized
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	pipeIn := os.Args[1]
	pipeOut := os.Args[2]

	fileIn, _ := os.OpenFile(pipeIn, os.O_RDONLY, 0666)
	defer fileIn.Close()

	fileOut, _ := os.OpenFile(pipeOut, os.O_WRONLY, 0666)
	defer fileOut.Close()

	scanner := bufio.NewScanner(fileIn)
	for scanner.Scan() {
		line := scanner.Text()
		capitalizedLine := strings.ToUpper(line) + "\n"
		_, err := fileOut.WriteString(capitalizedLine)
		if err != nil {
			fmt.Println("Error writing to output pipe:", err)
			os.Exit(1)
		}
	}

}
