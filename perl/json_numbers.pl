# Script takes string arguments and outputs a JSON array of numbers representing
# the length of each argument
use strict;
use warnings;
use JSON;

print encode_json([map { length } @ARGV]);
