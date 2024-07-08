package main

import (
	"encoding/json"
	"fmt"
	"log"
	"os"
)

type Person struct {
	FirstName string `json:"first_name"`
	Age       int64  `json:"age"`
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run main.go <json_file>")
		return
	}

	file := os.Args[1]
	data, err := os.ReadFile(file)
	if err != nil {
		log.Fatalf("Failed to read file: %v", err)
	}

	var people []Person
	if err := json.Unmarshal(data, &people); err != nil {
		log.Fatalf("Failed to parse JSON: %v", err)
	}

	for _, person := range people {
		fmt.Printf("Hello, %d year old %s\n", person.Age, person.FirstName)
	}
}
