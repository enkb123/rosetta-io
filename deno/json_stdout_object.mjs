// Script reads string args and transforms into python dict

const myStrings = Deno.args

// Make a dict with each string as a key and it's length as the value
const stringLengthDict = {}

for (const string of myStrings) {
  stringLengthDict[string] = string.length
}

console.log(JSON.stringify(stringLengthDict))
