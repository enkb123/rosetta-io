<?php

$outfile = $argv[1];
$text = $argv[2];

$uppercaseText = strtoupper($text);

file_put_contents($outfile, $uppercaseText);
