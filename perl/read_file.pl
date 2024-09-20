use strict;
use warnings;

my $file_path = './my-text-file.txt';
open my $fh, '<', $file_path;

while (my $line = <$fh>) {
    chomp $line;
    print "line: $line\n";

}

close $fh;
