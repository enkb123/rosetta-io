require 'json'

puts JSON.generate({
    "true" => true,
    "false" => false,
    "zero" => 0,
    "int" => 42,
    "float" => 3.14,
    "null" => nil,
    "empty string" => "",
    "a string with non-ascii characters" => "hello \n \u0001 world 🥸",
})

puts JSON.generate({
    "array of strings" => ["abc", "def", "ghi", "jkl"],
    "array of numbers" => [13, 42, 9000, -7],
    "array of nothing" => [],
    "array of mixed" => [13, "def", nil, false, ["a"], { "o" => 1}],
    "array of objects" => [
        { "name" => "Bob Barker", "age" => 84 },
        { "address1" => "123 Main St", "address2" => "Apt 1" },
    ],
    "array of arrays" => [
        ["a", "b", "c"],
        ["d", "e", "f"],
    ],
})

puts JSON.generate({
    "objects" => { "nested" => { "objects" => { "are" => "supported" } } },
})
