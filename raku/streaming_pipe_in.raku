use v6;

my $input = open "input.pipe", :r;

for $input.lines {
    say .uc;
    $*OUT.flush;
}

$input.close;
