<?php
$myStrings = array_slice($argv, 1);

$stringLettersDict = array_combine(
    $myStrings, array_map(
        fn($str) => str_split(strtoupper($str)), $myStrings
    )
);

echo json_encode($stringLettersDict);
