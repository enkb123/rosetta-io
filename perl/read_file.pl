# Read a file from file path (given as a command line arg),
# print line by line with line numbers
use strict;
use warnings;
print encode_json({ map { $_ => length($_) } @ARGV });
