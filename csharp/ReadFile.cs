
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
        var lines = File.ReadAllLines(filePath);
        lines.Select((line, index) => $"{index + 1} {line.ToUpper()}")
                .ToList()
                .ForEach(Console.WriteLine);
    }
}


