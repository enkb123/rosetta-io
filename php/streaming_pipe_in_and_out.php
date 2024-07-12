<?php
//Script reads text from a named pipe and writes it another named pipe, capitalized
$pipe_in = $argv[1];
$pipe_out = $argv[2];

$input_pipe = fopen($pipe_in, 'r');
$output_pipe = fopen($pipe_out, 'w');

stream_set_blocking($input_pipe, false);

while (true) {
    $line = fread($input_pipe, 1024);
    if ($line === false || feof($input_pipe)) {
        break;
    }
    fwrite($output_pipe, strtoupper($line));
    fflush($output_pipe);
}

fclose($input_pipe);
fclose($output_pipe);
?>
