using System;
using System.IO;

class ReadFile
{
    public static void Main(string[] args)
    {
        var filePath = "./my-text-file.txt";

        foreach (var line in File.ReadLines(filePath))
        {
            Console.WriteLine($"line: {line}");
        }
    }
}
