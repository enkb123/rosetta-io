import java.util.Scanner;
import java.util.stream.Stream;

public class Stdin {
    public static void main(String[] args) {
        var scanner = new Scanner(System.in);

        Stream.generate(scanner::nextLine)
              .forEach(line -> System.out.println("line: " + line));

        scanner.close();
    }
}
