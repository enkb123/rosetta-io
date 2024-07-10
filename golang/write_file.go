//Script to write text to a new file
//Run script as `go write_file.go <output_file>.txt 'some text'`

package main

import (
	"io/ioutil"
	"os"
	"strings"
)

func main() {

	outFile := os.Args[1]
	text := strings.ToUpper(os.Args[2])

	_ = ioutil.WriteFile(outFile, []byte(text), 0644)


}


