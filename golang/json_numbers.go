package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func main() {
	args := os.Args[1:]

	var lengths []int

	for _, arg := range args {
		lengths = append(lengths, len(arg))
	}

	jsonArrayBytes, _ := json.Marshal(lengths)

	fmt.Println(string(jsonArrayBytes))
}
