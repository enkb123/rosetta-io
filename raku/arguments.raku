# Script to read an argument and print as lowercase in stdout
use v6;

my $arg = @*ARGS[0];
say $arg.lc;
