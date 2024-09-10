require 'base64'

encoded_string = ARGV[0]

decoded_string = Base64.decode64(encoded_string)

puts decoded_string
