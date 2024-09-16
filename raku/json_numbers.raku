use v6;

use JSON::Fast;

say to-json(@*ARGS.map(*.chars));
