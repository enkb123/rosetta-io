local cjson = require("dkjson")

local file_path = arg[1]
local fh = io.open(file_path, "r")
local json_content = fh:read("*a")
fh:close()

local people = cjson.decode(json_content)

for _, person in ipairs(people) do
    print(string.format("Hello, %d year old %s", person.age, person.first_name))
end
