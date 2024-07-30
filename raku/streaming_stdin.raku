#Script reads streaming input text and then prints capitalized string to stdout
use v6;

for lines() {
    say .uc;
    $*OUT.flush;
}
