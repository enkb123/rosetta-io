require "json"

my_strings = ARGV

string_length_dict = my_strings.to_h do |string|
  {string, string.size}
end

puts string_length_dict.to_json
