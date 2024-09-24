local json = require("dkjson")

local filePath = "people.json"

local file = io.open(filePath, "r")
local jsonString = file:read("*a")
file:close()

local people, pos = json.decode(jsonString, 1, nil)

for _, person in ipairs(people) do
    print(string.format("Hello, %d year old %s", person.age, person.first_name))
end
