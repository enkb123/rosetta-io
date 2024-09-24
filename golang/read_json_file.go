package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func main() {
	filePath := "people.json"

	file, _ := os.Open(filePath)
	defer file.Close()

	var people []map[string]interface{}
	decoder := json.NewDecoder(file)
	decoder.Decode(&people)

	for _, person := range people {
		age := person["age"].(float64)
		firstName := person["first_name"].(string)
		fmt.Printf("Hello, %.0f year old %s\n", age, firstName)
	}
}
