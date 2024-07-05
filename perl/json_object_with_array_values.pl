use strict;
use warnings;
use JSON;

print JSON->new
    ->canonical(1)
    ->encode({ map { $_ => [split //, uc($_)] } @ARGV });
