require "base64"

encoded_string = ARGV[0]

puts Base64.decode_string(encoded_string)
