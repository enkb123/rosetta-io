const encodedString = Deno.args[0]

const decodedString = atob(encodedString)

console.log(decodedString)
