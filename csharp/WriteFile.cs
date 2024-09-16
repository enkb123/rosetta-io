using System;
using System.IO;

class WriteFile
{
    public static void Main(string[] args)
    {
        string outFile = args[0];
        string text = args[1].ToUpper();

        File.WriteAllText(outFile, text);
    }
}
