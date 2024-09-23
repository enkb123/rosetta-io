import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.*;

public class WriteToNamedPipe {
    public static void main(String[] args) throws IOException, InterruptedException{
        String pipePath = "output.pipe";

        Path path = Paths.get(pipePath);
        if (!Files.exists(path)) {
            new ProcessBuilder("mkfifo", pipePath).inheritIO().start().waitFor();
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(pipePath))) {
            writer.write("Hello World!");
        }
    }
}
