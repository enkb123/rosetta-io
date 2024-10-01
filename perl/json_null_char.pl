use strict;
use warnings;
use JSON;

my $json = JSON->new->utf8;

print $json->encode("Hello World \0");
