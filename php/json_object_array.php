<?php
$args = array_slice($argv, 1);

$myArray = array_map(function($arg) {
    return [strtoupper($arg) => strlen($arg)];
}, $args);

echo json_encode($myArray);
