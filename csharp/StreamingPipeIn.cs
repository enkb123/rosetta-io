using System;
using System.IO;

class StreamingPipeIn
{
    public static void Main(string[] args)
    {
        using var reader = new StreamReader("input.pipe");

        string line;
        while ((line = reader.ReadLine()) != null)
        {
            Console.WriteLine(line.ToUpper());
        }
    }
}
