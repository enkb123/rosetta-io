using System;
using System.IO;
using System.Diagnostics;

class WriteToNamedPipe
{
    public static void Main(string[] args)
    {
        using var writer = new StreamWriter("output.pipe") { AutoFlush = true };
        writer.WriteLine("Hello World!");
    }
}
