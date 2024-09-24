using System;
using System.IO;

class StreamingPipeInAndOut
{
    public static void Main(string[] args)
    {
        using var input = new StreamReader("streaming-in.pipe");
        using var output = new StreamWriter("streaming-out.pipe") { AutoFlush = true };

        string line;
        while ((line = input.ReadLine()) != null)
        {
            output.WriteLine($"received {line}");
        }
    }
}
