use strict;
use warnings;
use JSON;

my $file_path = './people.json';
open my $fh, '<', $file_path;

my $people = decode_json(do { local $/; <$fh> });

print "Hello, $_->{'age'} year old $_->{'first_name'}\n" for @$people;
