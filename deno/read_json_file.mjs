// Read JSON file, transform and print to stdout
const jsonFile = Deno.args[0];

const data = await Deno.readTextFile(jsonFile);

const people = JSON.parse(data);

for (const person of people) {
    console.log(`Hello, ${person.age} year old ${person.first_name}`);
}
