// Usage:
// Run a single script by specifying the script name as the first argument
// dotnet run <script_name>

// e.g.
// dotnet run arguments "hello world"
// dotnet run null_char

// To add more scripts, add a new case to the switch statement.
using System;

if (args.Length == 0)
{
    Console.Error.WriteLine("No command specified");
    return;
}

var scriptName = args[0];
var restOfArgs = args.Skip(1).ToArray();

Action<string[]> script = scriptName switch
{
    "arguments" => Arguments.Main,
    "null_char" => NullChar.Main,
    "stdin" => Stdin.Main,
    "read_file" => ReadFile.Main,
    "read_json_file" => ReadJsonFile.Main,
    "write_file" => WriteFile.Main,
    "json_array" => JsonArray.Main,
    "json_numbers" => JsonNumbers.Main,
    "json_stdout_object" => JsonStdoutObject.Main,
    "json_outputting_data" => JsonOutputtingData.Main,
    "json_object_with_array_values" => JsonObjectWithArrayValues.Main,
    "json_object_array" => JsonObjectArray.Main,
    "json_control_chars" => JsonControlChars.Main,
    "decode" => Decode.Main,
    "encode" => Encode.Main,
    "streaming_stdin" => StreamingStdin.Main,
    "streaming_pipe_in_and_out" => StreamingPipeInAndOut.Main,
    "streaming_pipe_in" => StreamingPipeIn.Main,
    "write_to_named_pipe" => WriteToNamedPipe.Main,
    _ => _ => Console.WriteLine("Unknown command " + scriptName)
};

script(restOfArgs);
