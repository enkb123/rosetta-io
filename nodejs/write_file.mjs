import fs from 'fs/promises'

const [outfile, text] = process.argv.slice(2)

await fs.writeFile(outfile, text.toUpperCase())
