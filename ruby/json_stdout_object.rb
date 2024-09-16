require 'json'

my_strings = ARGV

string_length_dict = my_strings.to_h { |string| [string, string.length] }

puts JSON.generate(string_length_dict)
