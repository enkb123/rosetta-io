using System;
using System.IO;
using System.Diagnostics;

class WriteToNamedPipe
{
    public static void Main(string[] args)
    {
        string pipePath = "output.pipe";

        if (!File.Exists(pipePath))
        {
            Process.Start("mkfifo", pipePath)?.WaitForExit();
        }

        using (var pipeStream = new FileStream(pipePath, FileMode.Open, FileAccess.Write))
        using (var writer = new StreamWriter(pipeStream) { AutoFlush = true })
        {
            writer.WriteLine("Hello World!");
        }
    }
}
