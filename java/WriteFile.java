//Script to write text to a new file
//Run script as `java write_file.java <output_file>.txt 'some text'`

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

public class WriteFile {
    public static void main(String[] args) throws IOException{
        if (args.length != 2) {
            System.err.println("Usage: java WriteFile.java <output_file>.txt 'some text'");
            System.exit(1);
        }

        String outFile = args[0];
        String text = args[1].toUpperCase();
        Files.write(Paths.get(outFile), text.getBytes(StandardCharsets.UTF_8));
    }
}
