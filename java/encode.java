//Script to encode a string as Base64

import java.util.Base64;

public class Base64Encoder {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java Base64Encoder <test_string>");
            System.exit(1);
        }

        String testString = args[0];
        byte[] encodedBytes = Base64.getEncoder().encode(testString.getBytes());

        // Create a string from the encoded bytes
        String encodedString = new String(encodedBytes);

        // Print the encoded string
        System.out.println(encodedString);
    }
}
