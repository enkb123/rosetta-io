// Script takes args and outputs a list of lengths

const myStrings = Deno.args

// Create an array of numbers based on the length of the string args
const stringLengths = myStrings.map((string) => string.length)

const jsonString = JSON.stringify(stringLengths)

console.log(jsonString)
