import { promises as fs } from 'fs';

const filePath = './my-text-file.txt'

const fileContent = await fs.readFile(filePath, 'utf8')

for (const line of fileContent.split("\n")) {
  if (line !== "") {
    console.log('line:', line);
  }
}
