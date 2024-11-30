require "json"

my_strings = ARGV

string_lengths = my_strings.map(&.size)

puts string_lengths.to_json
