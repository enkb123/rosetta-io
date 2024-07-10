// Script takes arguments and transforms them into dict with arrays as dict values
// and returns as JSON

package main

import (
	"encoding/json"
	"fmt"
	"os"
	"strings"
)

func main() {
	args := os.Args[1:]

	jsonObject := make(map[string][]string)

	for _, str := range args {
		var lettersArray []string
		for _, char := range strings.ToUpper(str) {
			lettersArray = append(lettersArray, string(char))
		}
		jsonObject[str] = lettersArray
	}

	jsonObjectBytes, _ := json.Marshal(jsonObject)

	fmt.Println(string(jsonObjectBytes))
}
