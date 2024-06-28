// Test script to get input, transform, and write to stdout

import java.util.Scanner;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Stream;

public class Stdin {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        AtomicInteger counter = new AtomicInteger(1);

        // Create a stream of lines from Scanner
        Stream.generate(scanner::nextLine)
              .takeWhile(line -> !line.isEmpty()) // Assuming empty line signals end, adjust as needed
              .forEach(line -> System.out.println(counter.getAndIncrement() + " " + line.toUpperCase()));

        scanner.close();
    }
}
