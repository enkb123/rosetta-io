for lines() {
    say "received $_";

    $*OUT.flush; # flush stdout
}
