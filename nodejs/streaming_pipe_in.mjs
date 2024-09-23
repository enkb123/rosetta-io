import * as fs from 'fs';
import * as readline from 'node:readline/promises';

const pipeIn = "input.pipe";

const input = fs.createReadStream(pipeIn);
const rl = readline.createInterface({ input })

for await (const line of rl) {
  console.log(line.toUpperCase())
}
