//Script to decode Base64 text
import java.util.Base64;

public class Decode {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java Base64Decoder <encoded_string>");
            System.exit(1);
        }

        String encodedString = args[0];
        byte[] decodedBytes = Base64.getDecoder().decode(encodedString);
        String decodedString = new String(decodedBytes);

        System.out.println(decodedString);
    }
}
