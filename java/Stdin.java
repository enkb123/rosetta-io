// Test script to get input, transform, and write to stdout
import java.util.Scanner;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Stream;

public class Stdin{
  public static void main(String[] args){
    Scanner scanner = new Scanner(System.in);
    AtomicInteger counter = new AtomicInteger(1);

    String line;
    do {
        line = scanner.nextLine();
        if (!line.isEmpty()) { // Skip processing if the line is empty
            System.out.println(counter.getAndIncrement() + " " + line.toUpperCase());
        }
    } while (scanner.hasNextLine());

    scanner.close();
}

}


