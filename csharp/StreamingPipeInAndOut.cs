using System;
using System.IO;
using System.IO.Pipes;

class StreamingPipeInAndOut
{
    public static void Main(string[] args)
    {
        string pipe_in = args[0];
        string pipe_out = args[1];

        using var input = new StreamReader(pipe_in);
        using var output = new StreamWriter(pipe_out) { AutoFlush = true };

        string line;
        while ((line = input.ReadLine()) != null)
        {
            output.WriteLine(line.ToUpper());
        }
    }
}
