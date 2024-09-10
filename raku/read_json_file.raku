use v6;
use JSON::Fast;

my $file-path = @*ARGS[0];

my $fh = open $file-path, :r;

my $people = from-json($fh.slurp-rest);

for @$people -> $person {
    say "Hello, {$person<age>} year old {$person<first_name>}";
}

$fh.close;
