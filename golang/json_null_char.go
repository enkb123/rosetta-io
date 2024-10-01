package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	str := "Hello World \x00"
	jsonData, _ := json.Marshal(str)
	fmt.Println(string(jsonData))
}
