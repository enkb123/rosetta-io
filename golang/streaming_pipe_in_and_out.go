package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	input, _ := os.Open("streaming-in.pipe")
	defer input.Close()

	output, _ := os.OpenFile("streaming-out.pipe", os.O_WRONLY, 0)
	defer output.Close()

	output.Sync()

	scanner := bufio.NewScanner(input)

	for scanner.Scan() {
		line := scanner.Text()
		fmt.Fprintf(output, "received %s\n", line)

	}
}
