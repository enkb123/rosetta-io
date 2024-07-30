# Script takes control characters and outputs valid JSON
use v6;

use JSON::Fast;

say to-json(@*ARGS[0]);
