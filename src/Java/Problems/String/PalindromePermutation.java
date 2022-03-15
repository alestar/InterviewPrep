package Java.Problems.String;

import java.util.HashSet;
import java.util.Set;

/**
Write an efficient method that checks whether any permutation ↴ of an input string is a palindrome. ↴
A palindrome is a string that's the same when read forward and backward.

Examples:
    civic
    mom
    anna
    kayak
    racecar

You can assume the input string only contains lowercase letters.

Examples:
    "civic" should return true
    "ivicc" should return true
    "civil" should return false
    "livci" should return false
    "But 'ivicc' isn't a palindrome!"

If you had this thought, read the question again carefully.
We're asking if any permutation of the string is a palindrome.
Spend some extra time ensuring you fully understand the question before starting.
Jumping in with a flawed understanding of the problem doesn't look good in an interview.
* */

public class PalindromePermutation {

    public static boolean hasPalindromePermutation(String theString) {

        // track characters we've seen an odd number of times
        Set<Character> unpairedCharacters = new HashSet<>();

        for (int i = 0; i < theString.length(); i++) {
            char c = theString.charAt(i);
            if (unpairedCharacters.contains(c)) {
                unpairedCharacters.remove(c);
            } else {
                unpairedCharacters.add(c);
            }
        }

        // the string has a palindrome permutation if it
        // has one or zero characters without a pair
        return unpairedCharacters.size() <= 1;
    }

    public static void main(String[] args) {
        System.out.println(" word 'civic' has palindrome permutation: " + hasPalindromePermutation("civic"));
        System.out.println(" word 'ivicc' has palindrome permutation: " + hasPalindromePermutation("ivicc"));
        System.out.println(" word 'kayak' has palindrome permutation: " + hasPalindromePermutation("kayak"));
        System.out.println(" word 'racecar' has palindrome permutation: " + hasPalindromePermutation("racecar"));
        System.out.println(" word 'civil' has palindrome permutation: " + hasPalindromePermutation("civil"));
        System.out.println(" word 'livci' has palindrome permutation: " + hasPalindromePermutation("livci"));

    }
}
