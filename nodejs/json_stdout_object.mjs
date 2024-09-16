const myStrings = process.argv.slice(2)

const stringLengthDict = {}

for (const string of myStrings) {
  stringLengthDict[string] = string.length
}

console.log(JSON.stringify(stringLengthDict))
