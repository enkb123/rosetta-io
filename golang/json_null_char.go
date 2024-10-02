package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	jsonData, _ := json.Marshal("Hello World \x00")
	fmt.Println(string(jsonData))
}
