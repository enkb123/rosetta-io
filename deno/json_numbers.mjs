const myStrings = Deno.args

const stringLengths = myStrings.map((string) => string.length)

const jsonString = JSON.stringify(stringLengths)

console.log(jsonString)
