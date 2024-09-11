<?php

$myStrings = array_slice($argv, 1);

$stringLengths = array_map('strlen', $myStrings);

echo json_encode($stringLengths);
