# Script takes args and turns into JSON array
use v6;

use JSON::Fast;

say to-json(@*ARGS);
