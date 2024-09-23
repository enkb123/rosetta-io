import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

public class WriteToTextFile {
    public static void main(String[] args) throws IOException{
        String outFile = "output.txt";
        String text = "Hello World!";
        Files.write(Paths.get(outFile), text.getBytes(StandardCharsets.UTF_8));
    }
}
