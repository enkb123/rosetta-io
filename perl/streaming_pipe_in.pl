use strict;
use warnings;

$| = 1;
open my $input, '<', "input.pipe";

print uc($_) while <$input>;

close $input;
