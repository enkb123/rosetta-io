require 'base64'

test_string = ARGV[0]

puts Base64.encode64(test_string)
