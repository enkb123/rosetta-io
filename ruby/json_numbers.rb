require 'json'

my_strings = ARGV

string_lengths = my_strings.map(&:length)

puts JSON.generate(string_lengths)
