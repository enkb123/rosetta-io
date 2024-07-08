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
    _ => _ => Console.WriteLine("Unknown command " + scriptName)
};

script(restOfArgs);
