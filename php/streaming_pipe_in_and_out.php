<?php

$output_pipe = fopen('streaming-out.pipe', 'w');
$input_pipe = fopen('streaming-in.pipe', 'r');

while (($line = fgets($input_pipe)) !== false) {
    fwrite($output_pipe, "received " . $line);
}

fclose($input_pipe);
fclose($output_pipe);
