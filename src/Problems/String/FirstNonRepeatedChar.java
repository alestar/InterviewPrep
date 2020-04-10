package Problems.String;
import java.util.HashMap;

public class FirstNonRepeatedChar {
    // Implement your solution below.
    public static Character nonRepeating(String s) {
        HashMap<Character, Integer> charCount = new HashMap<Character, Integer>();
        Character oneTimeChar=null;
        Integer count=0;
        boolean alreadyOne= false;

        // NOTE: Using s.toCharArray() is no the most efficient method,
        // but I chose to use it here for simplicity.
        for (char c : s.toCharArray()) {
            if (charCount.containsKey(c)) {
                Integer newVal = charCount.get(c) + 1;
                charCount.put(c, newVal);
            }
            else {
                charCount.put(c, 1);
                oneTimeChar= c;

            }
            if (charCount.get(c) > 1 && oneTimeChar!= null && c == oneTimeChar.charValue() ) {// case for one it found a duplicated char in the sequence, then reset oneTimeChar
                oneTimeChar = null;
            }

        }

        return oneTimeChar;
    }

    public static Character nonRepeatingIter(String s) {
        HashMap<Character, Integer> charCount = new HashMap<Character, Integer>();
        // NOTE: Using s.toCharArray() is no the most efficient method,
        // but I chose to use it here for simplicity.
        for (char c : s.toCharArray()) {
            if (charCount.containsKey(c)) {
                Integer newVal = charCount.get(c) + 1;
                charCount.put(c, newVal);
            } else {
                charCount.put(c, 1);
            }
        }
        for (char c : s.toCharArray()) {
            if (charCount.get(c) == 1) return c;
        }
        return null;
    }
    public static void main(String[] args) {
        // NOTE: The following input values will be used for testing your solution.

        System.out.println("For input : 'abcab' ");
        System.out.println("The output : " +  nonRepeating("abcab"));
        System.out.println("The output (Iter): " +  nonRepeatingIter("abcab")); // should return 'c'

        System.out.println("For input : 'abab' ");
        System.out.println("The output : " +  nonRepeating("abab"));
        System.out.println("The output (Iter): " +  nonRepeatingIter("abab")); // should return null

        System.out.println("For input : 'aabbbc' ");
        System.out.println("The output : " +  nonRepeating("aabbbc"));
        System.out.println("The output (Iter): " +  nonRepeatingIter("aabbbc")); // should return 'c'

        System.out.println("For input : 'aabbdbc' ");
        System.out.println("The output : " +  nonRepeating("aabbdbc"));
        System.out.println("The output (Iter): " +  nonRepeatingIter("aabbdbc")); // should return 'd'
    }
}
