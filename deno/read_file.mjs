// Read a file (file path given as a command line argument) and write to stdout

const filePath = Deno.args[0];
const file = await Deno.open(filePath);
const decoder = new TextDecoder();

let i = 1;
let partialLine = '';

for await (const chunk of Deno.iter(file)) {
    const chunkStr = decoder.decode(chunk, { stream: true });
    const lines = (partialLine + chunkStr).split('\n');

    for (const line of lines.slice(0, -1)) {
        console.log(`${i++} ${line.toUpperCase()}`);
    }

    partialLine = lines[lines.length - 1];
}

if (partialLine) {
    console.log(`${i} ${partialLine.toUpperCase()}`);
}

file.close();

