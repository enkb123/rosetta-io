
// Read a file from file path (given as a command line arg),
// print line by line with line numbers
using System;
using System.IO;
using System.Linq;

class ReadFile
{
    public static void Main (string[] args)
    {
        string filePath = args[0];
        int lineNumber = 1;
        var lines = File.ReadAllLines(filePath);
        lines.Select(line => $"{lineNumber++} {line.ToUpper()}")
                .ToList()
                .ForEach(Console.WriteLine);
    }
}


