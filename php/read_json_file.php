<?php

$filePath = 'people.json';

$jsonString = file_get_contents($filePath);

$people = json_decode($jsonString, true);

foreach ($people as $person) {
    $age = $person['age'];
    $firstName = $person['first_name'];
    echo "Hello, $age year old $firstName\n";
}
