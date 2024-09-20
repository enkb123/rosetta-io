import fs  from 'fs'
const path = './my-text-file.txt';

fs.readFile(path, 'utf8', (_, data) => {
    data.split('\n').forEach(line => {
    if (line.trim() !== '') {
      console.log(`line: ${line}`);
    }
  });
});
