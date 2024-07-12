package main

import (
	"encoding/json"
	"fmt"
	"os"
)

type Person struct {
	FirstName string `json:"first_name"`
	Age       int64  `json:"age"`
}

func main() {

	file := os.Args[1]
	data, _ := os.ReadFile(file)

	var people []Person
	json.Unmarshal(data, &people)

	for _, person := range people {
		fmt.Printf("Hello, %d year old %s\n", person.Age, person.FirstName)
	}
}
