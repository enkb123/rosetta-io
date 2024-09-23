use strict;
use warnings;

my ($outfile, $text) = ("output.txt", "Hello World!");

open my $fh, '>', $outfile or die "Cannot open!";

print $fh $text;
