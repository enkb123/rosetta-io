using System;
using System.IO;

class StreamingPipeIn
{
    public static void Main(string[] args)
    {
        string pipe_in = "input.pipe";
        using var reader = new StreamReader(pipe_in);

        string line;
        while ((line = reader.ReadLine()) != null)
        {
            Console.WriteLine(line.ToUpper());
        }
    }
}
