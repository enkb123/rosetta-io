use strict;
use warnings;

$| = 1;

while (my $input = <STDIN>) {
    chomp($input);
    print "received " . $input . "\n";
}
