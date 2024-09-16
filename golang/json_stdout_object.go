package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func main() {
	args := os.Args[1:]

	stringLengthMap := make(map[string]int)

	for _, arg := range args {
		stringLengthMap[arg] = len(arg)
	}

	jsonObjectBytes, _ := json.Marshal(stringLengthMap)
	fmt.Println(string(jsonObjectBytes))
}
