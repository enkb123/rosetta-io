import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.concurrent.atomic.AtomicInteger;

class ReadFile{
    public static void main(String[] args) throws IOException {
        var filePath = Paths.get(args[0]);
        var lineNumber = new AtomicInteger(1);

        Files.lines(filePath)
                .map(String::toUpperCase)
                .map(line -> lineNumber.getAndIncrement() + " " + line)
                .forEach(System.out::println);
    }
}
