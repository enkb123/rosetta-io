// Script reads text from a named pipe and writes it to stdout, capitalized

using System;
using System.IO;
using System.Text;

class StreamingPipeIn
{
    public static void Main(string[] args)
    {
        string pipe_in = args[0];

        using var reader = new StreamReader(args[0]);

        string line;
        while ((line = reader.ReadLine()) != null)
        {
            Console.WriteLine(line.ToUpper());
        }
    }
}
