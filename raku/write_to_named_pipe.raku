use v6;

my $fh = open "output.pipe", :w;
$fh.print: "Hello World!";
$fh.close;
