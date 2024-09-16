require 'base64'

test_string = ARGV[0]

encoded_string = Base64.encode64(test_string)

puts encoded_string
