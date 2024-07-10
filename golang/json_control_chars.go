//Script takes control characters and outputs valid JSON
package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func main() {
	testString := os.Args[1]

	jsonString, _ := json.Marshal(testString)

	fmt.Println(string(jsonString))
}
