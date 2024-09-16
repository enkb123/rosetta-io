use strict;
use warnings;
use JSON;

open my $fh, '<', $ARGV[0] or die "Cannot open file: $ARGV[0]\n";

my $people = decode_json(do { local $/; <$fh> });

print "Hello, $_->{'age'} year old $_->{'first_name'}\n" for @$people;
