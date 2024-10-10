using System;
using System.IO;

class WriteToTextFile
{
    public static void Main(string[] args)
    {
        File.WriteAllText("output.txt", "Hello World!");
    }
}
