// Test script to get input, transform, and write to stdout

using System;
using System.Collections.Generic;
using System.Linq;

public class Stdin
{
    public static void Main(string[] args)
    {
        List<string> lines = new List<string>();
        string line;
        while ((line = Console.ReadLine()) != null && line != "")
        {
            lines.Add(line);
        }

        int counter = 1;
        lines.ForEach(l => Console.WriteLine($"{counter++} {l.ToUpper()}"));
    }
}
