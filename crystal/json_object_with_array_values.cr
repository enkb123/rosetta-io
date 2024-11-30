require "json"

my_strings = ARGV

string_letters_dict = my_strings.to_h do |string|
  {string, string.upcase.split("")}
end

puts string_letters_dict.to_json
