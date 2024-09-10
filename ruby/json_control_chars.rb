require 'json'

test_string = ARGV[0]

puts JSON.generate(test_string)
