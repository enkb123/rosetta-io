// Script to decode Base64 text

const encodedString = Deno.args[0] // Get the Base64-encoded string from command-line arguments

const decodedString = atob(encodedString)

console.log(decodedString)
