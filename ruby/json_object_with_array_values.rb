require 'json'

my_strings = ARGV

string_letters_dict = my_strings.to_h { |string| [string, string.upcase.chars] }

puts JSON.generate(string_letters_dict)
