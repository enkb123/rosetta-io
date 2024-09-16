import java.util.Scanner;
import java.util.stream.Stream;

public class StreamingStdin {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Stream.generate(scanner::nextLine)
              .takeWhile(line -> !line.isEmpty())
              .map(String::toUpperCase)
              .forEach(System.out::println);
        scanner.close();
    }
}
