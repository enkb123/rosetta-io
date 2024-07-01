// Script takes args and turns into JSON array

const myStrings = Deno.args // Get command-line arguments, excluding 'node' and script name

console.log(JSON.stringify(myStrings))
