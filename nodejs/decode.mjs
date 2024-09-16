const encodedString = process.argv[2]

const decodedString = atob(encodedString)

console.log(decodedString)
