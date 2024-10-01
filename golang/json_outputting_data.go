package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	firstJsonObject := map[string]interface{}{
		"true":                               true,
		"false":                              false,
		"zero":                               0,
		"int":                                42,
		"float":                              3.14,
		"null":                               nil,
		"empty string":                       "",
		"a string with non-ascii characters": "hello \n \u0001 world 🥸",
	}

	secondJsonObject := map[string]interface{}{
		"array of strings": []string{"abc", "def", "ghi", "jkl"},
		"array of numbers": []int{13, 42, 9000, -7},
		"array of nothing": []interface{}{},
		"array of mixed": []interface{}{
			13, "def", nil, false, []string{"a"}, map[string]interface{}{"o": 1},
		},
		"array of objects": []interface{}{
			map[string]interface{}{"name": "Bob Barker", "age": 84},
			map[string]interface{}{"address1": "123 Main St", "address2": "Apt 1"},
		},
		"array of arrays": []interface{}{
			[]string{"a", "b", "c"},
			[]string{"d", "e", "f"},
		},
	}

	thirdJsonObject := map[string]interface{}{
		"objects": map[string]interface{}{
			"nested": map[string]interface{}{
				"objects": map[string]interface{}{
					"are": "supported",
				},
			},
		},
	}

	printJSON(firstJsonObject)
	printJSON(secondJsonObject)
	printJSON(thirdJsonObject)
}

func printJSON(data interface{}) {
	jsonData, _ := json.Marshal(data)
	fmt.Println(string(jsonData))
}
