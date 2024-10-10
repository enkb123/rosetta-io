import java.io.*;

public class StreamingPipeInAndOut {
    public static void main (String[] args) throws IOException {
        var inputPath = "streaming-in.pipe";
        var outputPath = "streaming-out.pipe";

        var input = new BufferedReader(new FileReader(inputPath));
        var output = new BufferedWriter(new FileWriter(outputPath));

        String line;
        while ((line = input.readLine()) != null) {
            output.write("received " + line + "\n");
            output.flush();
        }

        input.close();
        output.close();
    }
}
