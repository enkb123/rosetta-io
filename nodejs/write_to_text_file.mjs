import fs from 'fs/promises'

const [outfile, text] = ["output.txt", "Hello World!"]

await fs.writeFile(outfile, text)
