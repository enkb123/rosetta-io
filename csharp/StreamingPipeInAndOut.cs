//Script reads text from a named pipe and writes it another named pipe, capitalized
using System;
using System.IO;
using System.IO.Pipes;

class StreamingPipeInAndOut
{
    public static void Main(string[] args)
    {
        string pipe_in = args[0];
        string pipe_out = args[1];

            using (StreamReader input = new StreamReader(pipe_in))
            {
                using (StreamWriter output = new StreamWriter(pipe_out, append: false))
                {
                    string line;
                    while ((line = input.ReadLine()) != null)
                    {
                        string capitalizedLine = line.ToUpper();
                        output.WriteLine(capitalizedLine);
                        output.Flush(); // Ensure immediate write
                    }
                }
            }
    }
}
