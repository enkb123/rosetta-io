// Script reads text from a named pipe and writes it another named pipe, capitalized
import java.io.*;

public class StreamingPipeInAndOut {
    @SuppressWarnings("resource")
    public static void main (String[] args) throws IOException{
        String pipe_in = args[0];
        String pipe_out = args[1];

        BufferedReader input = new BufferedReader(new FileReader(pipe_in));
        BufferedWriter output = new BufferedWriter(new FileWriter(pipe_out));

        String line;
        while ((line = input.readLine()) != null) {
            output.write(line.toUpperCase());
            output.newLine();  // Ensure newline after each line
            output.flush();  // Flush to ensure immediate write
        }


    }
}
