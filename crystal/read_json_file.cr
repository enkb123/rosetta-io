require "json"

people = JSON.parse(File.read("people.json")).as_a || [] of Hash(String, JSON::Any)

people.each do |person|
  age = person["age"].as_i
  first_name = person["first_name"].as_s
  puts "Hello, #{age} year old #{first_name}"
end
