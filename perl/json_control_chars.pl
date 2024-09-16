use strict;
use warnings;
use JSON;

print JSON->new->encode($ARGV[0]);
