<?php
$myStrings = array_slice($argv, 1);

$stringLengthDict = array_combine($myStrings, array_map('strlen', $myStrings));

echo json_encode($stringLengthDict) . "\n";
