const myStrings = process.argv.slice(2)

const stringLengths = myStrings.map((string) => string.length)

const jsonString = JSON.stringify(stringLengths)

console.log(jsonString)
