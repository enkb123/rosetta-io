use v6;

my $pipe-path = 'output.pipe';

my $path = IO::Path.new($pipe-path);
if !$path.e {
    run "mkfifo", $pipe-path;
}

my $pipe = open $pipe-path, :w;

$pipe.print("Hello World!\n");

$pipe.close;
