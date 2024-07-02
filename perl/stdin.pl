# Test script to get input, transform, and write to stdout
use strict;
use warnings;

my $i = 1;
print $i++ . " " . uc while <STDIN>;
