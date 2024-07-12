// Test script to get input, transform, and write to stdout

using System;
using System.Collections.Generic;
using System.Linq;

class Stdin
{
    public static void Main(string[] args)
    {
        List<string> lines = new List<string>();
        string line;
        int counter = 1;
        while (!string.IsNullOrEmpty(line = Console.ReadLine())){
                Console.WriteLine($"{counter++} {line.ToUpper()}");
            }
    }
}
