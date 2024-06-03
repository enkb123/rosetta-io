use strict;
use warnings;
$| = 1;  # Turn off output buffering

while (my $input = <STDIN>) {
    print uc($input);
}
