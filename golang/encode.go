//Script to encode a string as Base64

package main

import (
	"encoding/base64"
	"fmt"
	"os"
)

func main() {
	fmt.Println(base64.StdEncoding.EncodeToString([]byte(os.Args[1])))
}
