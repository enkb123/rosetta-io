// Script takes control characters and outputs valid JSON

const myString = Deno.args[0]

console.log(JSON.stringify(myString))
