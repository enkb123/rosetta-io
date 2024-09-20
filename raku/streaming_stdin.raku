while (my $input = $*IN.get) {
    say "received " ~ $input;
    $*OUT.flush;
}
