// Script outputs arrays of objects as JSON

package main

import (
	"encoding/json"
	"fmt"
	"os"
	"strings"
)

func main() {
	args := os.Args[1:]

	var arrayNode []map[string]interface{}

	for _, str := range args {
		obj := make(map[string]interface{})
		obj[strings.ToUpper(str)] = len(str)
		arrayNode = append(arrayNode, obj)
	}

	jsonArrayBytes, _ := json.Marshal(arrayNode)

	fmt.Println(string(jsonArrayBytes))
}
