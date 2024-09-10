use strict;
use warnings;

$| = 1;

my ($pipe_in) = @ARGV;

open my $input, '<', $pipe_in or die "Cannot open input pipe: $!";

while (my $line = <$input>) {
    print uc($line);
}

close $input;
