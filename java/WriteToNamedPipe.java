import java.nio.charset.StandardCharsets;
import java.nio.file.*;

public class WriteToNamedPipe {
    public static void main(String[] args) throws Exception {
        var outFile = Paths.get("output.pipe");
        var text = "Hello World!";
        Files.write(outFile, text.getBytes(StandardCharsets.UTF_8));
    }
}
