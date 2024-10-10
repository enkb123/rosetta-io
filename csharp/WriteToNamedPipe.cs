using System;
using System.IO;

class WriteToNamedPipe
{
    public static void Main(string[] args)
    {
        File.WriteAllText("output.pipe", "Hello World!");
    }
}
