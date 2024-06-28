
// Read a file from file path (given as a command line arg),
// print line by line with line numbers
import java.io.*;

class ReadFile{
    public static void main(String[] args) throws FileNotFoundException, IOException{
        String filePath = args[0];
            try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
                String line;
                int i = 1;
                while ((line = reader.readLine()) != null) {
                    System.out.println(i + " " + line.toUpperCase());
                    i++;
                }
            }
    }
}
