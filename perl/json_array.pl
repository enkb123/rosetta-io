# Script takes args and turns into JSON array
use strict;
use warnings;
use JSON;

print encode_json(\@ARGV);
