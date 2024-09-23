use v6;

my $file-path = './my-text-file.txt';

for $file-path.IO.lines {
    say "line: $_";
}
