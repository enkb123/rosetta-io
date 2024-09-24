use strict;
use warnings;

open my $fh, '>', "output.txt";
print $fh "Hello World!";
close $fh;
