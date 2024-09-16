const testString = Deno.args[0]

const encodedString = btoa(testString)

console.log(encodedString)
