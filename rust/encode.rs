//Script to encode a string as Base64

import java.util.Base64;

public class Encode {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java Encode.java <test_string>");
            System.exit(1);
        }

        String testString = args[0];
        String encodedString = Base64.getEncoder().encodeToString(testString.getBytes());



        // Print the encoded string
        System.out.println(encodedString);
    }
}
