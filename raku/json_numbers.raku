# Script takes string arguments and outputs a JSON array of numbers representing the length of each argument
use v6;

use JSON::Fast;

say to-json(@*ARGS.map(*.chars));
