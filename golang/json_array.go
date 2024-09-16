package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func main() {
	args := os.Args[1:]

	var jsonArray []string

	for _, arg := range args {
		jsonArray = append(jsonArray, arg)
	}

	jsonArrayBytes, _ := json.Marshal(jsonArray)

	fmt.Println(string(jsonArrayBytes))
}
