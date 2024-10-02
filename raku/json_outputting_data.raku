use JSON::Fast;

my %first-json-object = {
    'true'                    => True,
    'false'                   => False,
    'zero'                    => 0,
    'int'                     => 42,
    'float'                   => 3.14,
    'null'                    => Nil,
    'empty string'            => '',
    'a string with non-ascii characters' => "hello \n \x01 world 🥸"
};

my %second-json-object = {
    'array of strings' => ['abc', 'def', 'ghi', 'jkl'],
    'array of numbers' => [13, 42, 9000, -7],
    'array of nothing' => [],
    'array of mixed'   => [13, 'def', Nil, False, ['a'], {'o' => 1 }],
    'array of objects' => [
        { 'name' => 'Bob Barker', 'age' => 84 },
        { 'address1' => '123 Main St', 'address2' => 'Apt 1' },
    ],
    'array of arrays' => [
        ['a', 'b', 'c'],
        ['d', 'e', 'f']
    ]
};

my %third-json-object = {
    'objects' => {
        'nested' => {
            'objects' => {
                'are' => 'supported'
            }
        }
    }
};

say to-json(%first-json-object, :pretty(False));
say to-json(%second-json-object, :pretty(False));
say to-json(%third-json-object, :pretty(False));
