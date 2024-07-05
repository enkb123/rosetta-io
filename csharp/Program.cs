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
