require "json"

my_strings = ARGV

my_array = my_strings.map { |string| { string.upcase => string.size } }

puts my_array.to_json
