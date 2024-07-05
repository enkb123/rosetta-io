// Script to encode a string as Base64

const testString = Deno.args[0] // Get the Base64-encoded string from command-line arguments

const encodedString = btoa(testString)

console.log(encodedString)
