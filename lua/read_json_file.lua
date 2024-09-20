local cjson = require("dkjson")

local filePath = "people.json"

local function readFile(filePath)
    local file = io.open(filePath, "r")
    local content = file:read("*a")
    file:close()
    return content
end

local jsonString = readFile(filePath)
local people, pos = cjson.decode(jsonString, 1, nil)

for _, person in ipairs(people) do
    print(string.format("Hello, %d year old %s", person.age, person.first_name))
end
