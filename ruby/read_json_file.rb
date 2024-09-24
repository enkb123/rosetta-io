require 'json'

people = JSON.load_file("people.json")

people.each do |person|
  puts "Hello, #{person['age']} year old #{person['first_name']}"
end
