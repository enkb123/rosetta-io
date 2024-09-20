import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadFile {
    public static void main(String[] args) throws IOException{
        String filePath = "./my-text-file.txt";

        BufferedReader br = new BufferedReader(new FileReader(filePath));
        String line;
        while ((line = br.readLine()) != null) {
            if (!line.isEmpty()) {
                System.out.println("line: " + line);
            }

        }
    }
}
