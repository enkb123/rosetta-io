import java.nio.charset.StandardCharsets;
import java.nio.file.*;

public class WriteToTextFile {
    public static void main(String[] args) throws Exception {
        var outFile = Paths.get("output.txt");
        var text = "Hello World!";
        Files.write(outFile, text.getBytes(StandardCharsets.UTF_8));
    }
}
