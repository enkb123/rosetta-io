use v6;
use JSON::Fast;

my $file-path = "people.json";

my $people = from-json $file-path.IO.slurp;

for @$people -> $person {
    say "Hello, {$person<age>} year old {$person<first_name>}";
}
