//Script to write text to a new file
//Run script as `java write_file.java <output_file>.txt 'some text'`


import java.io.FileWriter;
import java.io.IOException;

public class WriteFile {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.err.println("Usage: java WriteFile.java <output_file>.txt 'some text'");
            System.exit(1);
        }

        String outFile = args[0];
        String text = args[1].toUpperCase();

        try {
            FileWriter writer = new FileWriter(outFile);
            writer.write(text);
            writer.close();
        } catch (IOException e) {
            System.err.println("An error occurred while writing to the file.");
            e.printStackTrace();
        }
    }
}
