require 'json'

my_strings = ARGV

my_array = my_strings.map { |string| {string.upcase => string.length} }

puts JSON.generate(my_array)
