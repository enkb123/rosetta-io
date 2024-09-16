const args = process.argv.slice(2)

const myArray = args.map((arg) => ({ [arg.toUpperCase()]: arg.length }))

console.log(JSON.stringify(myArray))
