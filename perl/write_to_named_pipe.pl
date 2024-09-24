use strict;
use warnings;

open my $fh, '>', "output.pipe";
print $fh "Hello World!";
close $fh;
