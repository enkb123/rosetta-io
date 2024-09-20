const filePath = "./my-text-file.txt";
const fileContent = await Deno.readTextFile(filePath);

for (const line of fileContent.split("\n")) {
  if (line.trim() !== "") {
    console.log(`line: ${line}`);
  }
}
