using System;
using System.IO;

class WriteToTextFile
{
    public static void Main(string[] args)
    {
        string outFile = "output.txt";
        string text = "Hello World!";

        File.WriteAllText(outFile, text);
    }
}
