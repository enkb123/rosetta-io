<?php

$filePath = 'people.json';

$jsonData = file_get_contents($filePath);

$people = json_decode($jsonData);

foreach ($people as $person) {
    echo "Hello, {$person->age} year old {$person->first_name}\n";
}
