import * as fs from 'fs';
import * as readline from 'node:readline/promises';

const inputStream = fs.createReadStream('streaming-in.pipe');
const outputStream = fs.createWriteStream('streaming-out.pipe');

const rl = readline.createInterface({ input: inputStream });

for await (const line of rl) {
  outputStream.write(`received ${line}\n`);
}

outputStream.end();
