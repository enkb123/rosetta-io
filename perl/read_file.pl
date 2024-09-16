use strict;
use warnings;

my $file_path = shift;

open my $fh, '<', $file_path or die "Cannot open file: $file_path\n";

my $i = 1;
print $i++ . " " . uc while <$fh>;
