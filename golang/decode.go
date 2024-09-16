package main

import (
	"encoding/base64"
	"fmt"
	"os"
)

func main() {
	decodedBytes, _ := base64.StdEncoding.DecodeString(os.Args[1])

	fmt.Println(string(decodedBytes))
}
