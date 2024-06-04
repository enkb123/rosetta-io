# Read a file from file path (given as a command line arg),
# print line by line with line numbers

use strict;
use warnings;

my $file_path = $ARGV[0];

eval {
    open(my $fh, '<', $file_path) or die "Cannot open file: $!";
    my $i = 1;
    while (my $line = <$fh>) {
        print "$i " . uc($line);
        $i++;
    }
    close($fh);
};

if ($@) {
    if ($@ =~ /No such file or directory/) {
        print "File not found: $file_path\n";
        exit(1);
    } else {
        die $@;
    }
}


