import java.io.*;

public class StreamingPipeIn {
    public static void main(String[] args) throws IOException {
        String pipe_in = args[0];

        BufferedReader input = new BufferedReader(new FileReader(pipe_in));

        String line;
        while ((line = input.readLine()) != null) {
            System.out.println(line.toUpperCase());
        }

        input.close();
    }
}
