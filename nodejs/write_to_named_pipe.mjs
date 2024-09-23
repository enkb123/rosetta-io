import fs from 'fs';

const [pipeName, text] = ["output.pipe", "Hello World!"];

const writeToPipe = (pipe, data) => {
    return new Promise((resolve) => {
        const writableStream = fs.createWriteStream(pipe);
        writableStream.on('finish', resolve);
        writableStream.write(data);
        writableStream.end();
    });
};

writeToPipe(pipeName, text)
