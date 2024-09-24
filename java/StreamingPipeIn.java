import java.io.*;

public class StreamingPipeIn {
    public static void main(String[] args) throws Exception {
        var pipe_in = "input.pipe";

        var input = new BufferedReader(new FileReader(pipe_in));

        String line;
        while ((line = input.readLine()) != null) {
            System.out.println(line.toUpperCase());
        }

        input.close();
    }
}
