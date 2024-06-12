// Script reads streaming input text and then prints capitalized string to stdout

import java.util.Scanner;

public class StreamingStdin {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNextLine()) {
            String input = scanner.nextLine();
            System.out.println(input.toUpperCase());
        }
    }
}
