# Script reads text from a named pipe and writes it to stdout, capitalized

use strict;
use warnings;

$| = 1;  # Turn off output buffering

my ($pipe_in) = @ARGV;

open my $input, '<', $pipe_in or die "Cannot open input pipe: $!";

while (my $line = <$input>) {
    print uc($line);
}

close $input;
