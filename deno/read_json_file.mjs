const filePath = "./people.json";

const data = await Deno.readTextFile(filePath);

const people = JSON.parse(data);

for (const person of people) {
    console.log(`Hello, ${person.age} year old ${person.first_name}`);
}
