using System;
using System.IO;

class StreamingPipeInAndOut
{
    public static void Main(string[] args)
    {
        using (FileStream outputStream = new FileStream("streaming-out.pipe", FileMode.Create, FileAccess.Write))
        using (StreamWriter output = new StreamWriter(outputStream) { AutoFlush = true })
        {
            using (FileStream inputStream = new FileStream("streaming-in.pipe", FileMode.Open, FileAccess.Read))
            using (StreamReader input = new StreamReader(inputStream))
            {
                string line;
                while ((line = input.ReadLine()) != null)
                {
                    output.WriteLine($"received {line}");
                }
            }
        }
    }
}
