use strict;
use warnings;

my $file_path = './my-text-file.txt';
open my $fh, '<', $file_path;

print "line: $_" while <$fh>;
