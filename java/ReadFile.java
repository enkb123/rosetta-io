import java.nio.file.Files;
import java.nio.file.Paths;

public class ReadFile {
    public static void main(String[] args) throws Exception {
        var filePath = Paths.get("./my-text-file.txt");

        Files.lines(filePath)
            .forEach(line -> System.out.println("line: " + line));
    }
}
