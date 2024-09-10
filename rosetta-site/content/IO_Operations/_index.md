+++
title = 'I/O Operations'
draft = false
+++

### I/O operations and serialization format examples
[ arguments ]({{< ref "arguments" >}}) : Test that args can be passed to script

[ decode ]({{< ref "decode" >}}) : Test that base64 can be decoded as a string

[ encode ]({{< ref "encode" >}}) : Test that a string can be encoded as base64

[ json_array ]({{< ref "json_array" >}}) : Test that JSON array is parsed correctly

[ json_control_chars ]({{< ref "json_control_chars" >}}) : Test that control characters and emojis are output in valid JSON
note: control character "\0" is used by C (and Python) to end strings and so we can't
pass it as argument in the test string because it will raise "invalid argument" error


[ json_numbers ]({{< ref "json_numbers" >}}) : Test that JSON list of numbers is parsed correctly

[ json_object_array ]({{< ref "json_object_array" >}}) : Test that a JSON array made of objects is parsed correctly

[ json_object_with_array_values ]({{< ref "json_object_with_array_values" >}}) : Test that a JSON object with arrays as values is parsed correctly

[ json_stdout_object ]({{< ref "json_stdout_object" >}}) : Test that JSON object is parsed correctly

[ null_char ]({{< ref "null_char" >}}) : Test outputing a null character

[ read_file ]({{< ref "read_file" >}}) : Check that a file is read line by line, when file path is given
as command line argument


[ read_json_file ]({{< ref "read_json_file" >}}) : Test that a JSON file is read correctly

[ stdin ]({{< ref "stdin" >}}) : Check that input is read from stdin, line by line.
The script executed in the docker container accepts a text file as input,
reads each line, capitalizes it, then prints it out.


[ streaming_pipe_in ]({{< ref "streaming_pipe_in" >}}) : Test that named pipe can be read line by line and can write to stdout

[ streaming_pipe_in_and_out ]({{< ref "streaming_pipe_in_and_out" >}}) : Test that named pipe can be read line by line and can write to output pipe without waiting for all lines to arrive

[ streaming_stdin ]({{< ref "streaming_stdin" >}}) : Test that streaming stdin can be read line by line and can write to stdout
without waiting for all lines to arrive

[ write_file ]({{< ref "write_file" >}}) : Test that a script, given a path to a named pipe, can write to that named pipe

