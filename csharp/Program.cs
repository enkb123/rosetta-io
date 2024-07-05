// Usage:
// Run a single script by specifying the script name as the first argument
// dotnet run <script_name>

// e.g.
// dotnet run arguments "hello world"
// dotnet run null_char

// To add more scripts, add a new case to the switch statement.

if (args.Length == 0) {
    Console.Error.WriteLine("No command specified");
    return;
}

var restOfArgs = args.Skip(1).ToArray();

switch (args[0]) {
    case "arguments": Arguments.Main(restOfArgs);
        break;
    case "null_char": NullChar.Main(restOfArgs);
        break;
    default:
        Console.WriteLine("Unknown command " + args[0]);
        break;
}
