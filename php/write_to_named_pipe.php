<?php

$pipePath = 'output.pipe';

if (!file_exists($pipePath)) {
    posix_mkfifo($pipePath, 0666);
}

$pipe = fopen($pipePath, 'w') or die("Could not open '$pipePath'");

fwrite($pipe, "Hello World!\n");

fclose($pipe);
