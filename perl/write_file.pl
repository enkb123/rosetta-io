# Script to write text to a new file
# Run script as `perl write_file.pl <output_file>.txt 'some text'`
use strict;
use warnings;

my ($outfile, $text) = @ARGV;

open my $fh, '>', $outfile or die "Cannot open $ARGV[0]: $!";

print $fh uc $text;
