package MyJava.PastInverview.Turing;

/**
 * Given a string, find the length of the longest substring without repeating characters.
 *
 * Examples:
 *
 * Given "abcabcbb", the answer is "abc", which the length is 3.
 * Given "bbbbb", the answer is "b", with the length of 1.
 * Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
 *
 * @author Alestar
 *
 *
 * Explanation:
 *
 * We use an integer array index of size 128 (to cover all ASCII characters) is used to store the last seen position of each character in the string.
 * We maintain a sliding window [i, j] (j = j + 1 in each iteration) and move i to the right side of the last seen position of s[j] if needed.
 * We also update the result if we get a longer substring.
 *
 * Time complexity: O(n)
 * Space complexity: O(1)
 *
 *
 */
public class LongestSubStringWithoutRepeatingChar{
    public int lengthOfLongestSubStrWithoutRepHashSet(String s) {
        int n = s.length();
        int ans = 0;
        java.util.Set<Character> set = new java.util.HashSet<>();
        int i = 0, j = 0;
        while (i < n && j < n) {
            // try to extend the range [i, j]
            if (!set.contains(s.charAt(j))){
                set.add(s.charAt(j++));
                ans = Math.max(ans, j - i);
            }
            else {
                set.remove(s.charAt(i++));
            }
        }
        return ans;
    }
    public int lengthOfLongestSubStrWithoutRepOptimal(String s) {
        int n = s.length();
        int ans = 0;
        //An array index of size 128 (to cover all ASCII characters) is used to store the last seen position of each character in the string.
        int[] index = new int[128]; // current index of character
        // try to extend the range [i, j]
        for (int j = 0, i = 0; j < n; j++) {
            System.out.println("char at : " +  s.charAt(j));
            System.out.println("char index : " +  index[s.charAt(j)]);

            //For each character s[j], the method checks if it has been seen before within the current window ([i, j]).
            //If it has, the start of the window (i) is updated to the maximum of its current value and the position after the last occurrence of s[j] (index[s.charAt(j)]).
            i = Math.max(index[s.charAt(j)], i);
            ans = Math.max(ans, j - i + 1);
            index[s.charAt(j)] = j + 1;
        }
        return ans;
    }

    public static  void main(String[] args) {

        LongestSubStringWithoutRepeatingChar s = new LongestSubStringWithoutRepeatingChar();
        System.out.println("Result (HashSet): " + s.lengthOfLongestSubStrWithoutRepHashSet("abcabcbb"));
        System.out.println("Result (HashSet): " + s.lengthOfLongestSubStrWithoutRepHashSet("bbbb"));
        System.out.println("Result (Optimal): " + s.lengthOfLongestSubStrWithoutRepOptimal("abcabcbb"));
        System.out.println("Result (Optimal): " + s.lengthOfLongestSubStrWithoutRepOptimal("bbbb"));



    }
}
