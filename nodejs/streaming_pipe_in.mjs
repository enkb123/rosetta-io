//Script reads text from a named pipe and writes it to stdout, capitalized

import * as fs from 'fs';
import * as readline from 'node:readline/promises';

const pipeIn = process.argv[2];

const input = fs.createReadStream(pipeIn);
const rl = readline.createInterface({ input })

for await (const line of rl) {
  console.log(line.toUpperCase())
}
