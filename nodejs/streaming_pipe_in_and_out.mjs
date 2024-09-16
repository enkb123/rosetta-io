import * as fs from 'fs';
import * as readline from 'node:readline/promises';

const pipeIn = process.argv[2];
const pipeOut = process.argv[3];

const input = fs.createReadStream(pipeIn);
const rl = readline.createInterface({ input })

const output = fs.createWriteStream(pipeOut);

for await(const line of rl){
  output.write(line.toUpperCase() + '\n');
}
