// Test script to get input, transform, and write to stdout
import java.util.Scanner;

public class Main{
  public static void main(String[] args){
    int i = 1;
    Scanner scanner = new Scanner(System.in);
    while (scanner.hasNextLine()) {
        String userInput = scanner.nextLine();
        System.out.println(i + " " + userInput.toUpperCase());
        i++;
  }
}
}
