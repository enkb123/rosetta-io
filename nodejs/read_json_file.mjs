import fs  from 'fs'

const filePath = './people.json';

fs.readFile(filePath, 'utf8', (_, data) => {

  const people = JSON.parse(data);

  people.forEach(person => {
      console.log(`Hello, ${person.age} year old ${person.first_name}`);
  });

});
