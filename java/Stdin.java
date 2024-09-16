import java.util.Scanner;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Stream;

public class Stdin {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        AtomicInteger counter = new AtomicInteger(1);

        Stream.generate(scanner::nextLine)
              .takeWhile(line -> !line.isEmpty())
              .forEach(line -> System.out.println(counter.getAndIncrement() + " " + line.toUpperCase()));

        scanner.close();
    }
}
