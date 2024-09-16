import * as readline from 'node:readline/promises'
import fs  from 'fs'

const file_path = process.argv[2]

const rl = readline.createInterface({
  input: fs.createReadStream(file_path),
})

let i = 1
for await (const line of rl) {
  console.log(i + " " + line.toUpperCase())
  i++
}
