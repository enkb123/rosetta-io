use v6;

my $file-path = './my-text-file.txt';
my $file = $file-path.IO;

if $file ~~ :e {
    for $file.lines {
        say "line: $_";

    }
}
