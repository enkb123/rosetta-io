// Script to read an argument and print as lowercase in stdout

package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Println(strings.ToLower(os.Args[1]))
}
