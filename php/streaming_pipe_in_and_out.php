<?php

$inputFile = 'streaming-in.pipe';
$outputFile = 'streaming-out.pipe';

$output_pipe = fopen($outputFile, 'w');
$input_pipe = fopen($inputFile, 'r');

while (($line = fgets($input_pipe)) !== false) {
    fwrite($output_pipe, "received " . $line);
}

fclose($input_pipe);
fclose($output_pipe);
