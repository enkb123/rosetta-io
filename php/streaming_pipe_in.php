<?php
// Script reads text from a named pipe and writes it to stdout, capitalized
$pipe_in = $argv[1];

$input_pipe = fopen($pipe_in, 'r');

stream_set_blocking($input_pipe, false);

while (true) {
    $line = fread($input_pipe, 1024);
    if ($line === false || feof($input_pipe)) {
        break;
    }
    echo strtoupper($line);
}

fclose($input_pipe);
?>
