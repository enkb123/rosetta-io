use strict;
use warnings;

my ($outfile, $text) = @ARGV;

open my $fh, '>', $outfile or die "Cannot open $ARGV[0]: $!";

print $fh uc $text;
