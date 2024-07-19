#Script reads streaming input text and then prints capitalized string to stdout
use v6;

$*OUT.flush;

for lines() {
    say .uc;
}
