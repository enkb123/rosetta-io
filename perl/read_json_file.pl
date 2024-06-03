# Read JSON file, transform and print to stdout
use strict;
use warnings;
use JSON;
open(my $fh,'<',$ARGV[0]);
my$people=decode_json(do{local$/;<$fh>});
foreach my $person(@$people){print "Hello, ".$person->{'age'}." year old ".$person->{'first_name'}."\n";}
