# Test script to get input, transform, and write to stdout
use v6;

my $i = 1;
for lines() {
    say $i++ ~ " " ~ .uc;
}
