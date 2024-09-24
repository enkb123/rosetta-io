import java.util.Scanner;
import java.util.stream.Stream;

public class StreamingStdin {
    public static void main(String[] args) {
        var scanner = new Scanner(System.in);

        Stream.generate(scanner::nextLine)
              .forEach(line -> System.out.println("received " + line));

        scanner.close();
    }
}
