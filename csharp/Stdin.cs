using System;
using System.Collections.Generic;
using System.Linq;

class Stdin
{
    public static void Main(string[] args)
    {
        string line;
        int counter = 1;
        while ((line = Console.ReadLine()) != null)
        {
            Console.WriteLine($"{counter++} {line.ToUpper()}");
        }
    }
}
