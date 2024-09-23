import java.io.*;

public class StreamingPipeInAndOut {
    public static void main (String[] args) throws IOException{
        String inputPath = "streaming-in.pipe";
        String outputPath = "streaming-out.pipe";

        BufferedReader input = new BufferedReader(new FileReader(inputPath));
        BufferedWriter output = new BufferedWriter(new FileWriter(outputPath));

        String line;
        while ((line = input.readLine()) != null) {
            output.write("received " + line);
            output.newLine();
            output.flush();
        }

        input.close();
        output.close();
    }
}
