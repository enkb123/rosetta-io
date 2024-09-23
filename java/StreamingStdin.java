import java.util.Scanner;
import java.util.stream.Stream;

public class StreamingStdin {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Stream.generate(scanner::nextLine)
              .takeWhile(line -> !line.isEmpty())
              .forEach(line -> System.out.println("received " + line));

        scanner.close();
    }
}
