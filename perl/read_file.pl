# Read a file from file path (given as a command line arg),
# print line by line with line numbers

use strict;
use warnings;

my $file_path = shift;

open my $fh, '<', $file_path or die "Cannot open file: $file_path\n";

my $i = 1;
print $i++ . " " . uc while <$fh>;
