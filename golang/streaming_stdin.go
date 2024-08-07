// Script reads streaming input text and then prints capitalized string to stdout

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		fmt.Println(strings.ToUpper(scanner.Text()))
	}
}
