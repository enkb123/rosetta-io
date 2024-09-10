use strict;
use warnings;
use JSON;

print encode_json([map { length } @ARGV]);
