# Test script to get input, transform, and write to stdout
use strict;
use warnings;
my $i = 1;

while (my $user_input = <STDIN>) {
  print "$i " . uc($user_input);
  $i++;
}

