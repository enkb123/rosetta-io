<?php

$pipe_in = $argv[1];
$pipe_out = $argv[2];

$input_pipe = fopen($pipe_in, 'r');
$output_pipe = fopen($pipe_out, 'w');

while (($line = fgets($input_pipe)) !== false) {
    fwrite($output_pipe, strtoupper($line));
    fflush($output_pipe);
}

fclose($input_pipe);
fclose($output_pipe);
?>
