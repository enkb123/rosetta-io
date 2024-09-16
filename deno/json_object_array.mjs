const args = Deno.args

const myArray = args.map((arg) => ({ [arg.toUpperCase()]: arg.length }))

console.log(JSON.stringify(myArray))
