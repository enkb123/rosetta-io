package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println("1st argument: " + os.Args[1])
	fmt.Println("2nd argument: " + os.Args[2])

}
