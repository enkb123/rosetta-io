import java.util.Base64;

public class Decode {
    public static void main(String[] args) {
        String encodedString = args[0];
        byte[] decodedBytes = Base64.getDecoder().decode(encodedString);
        String decodedString = new String(decodedBytes);

        System.out.println(decodedString);
    }
}
