package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	output, _ := os.OpenFile("streaming-out.pipe", os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0644)
	defer output.Close()

	output.Sync()

	input, _ := os.Open("streaming-in.pipe")
	defer input.Close()

	scanner := bufio.NewScanner(input)

	for scanner.Scan() {
		line := scanner.Text()
		fmt.Fprintf(output, "received %s\n", line)

	}
}
