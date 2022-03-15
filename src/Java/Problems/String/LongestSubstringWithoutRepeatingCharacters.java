package Java.Problems.String;

import java.util.HashSet;
import java.util.Set;

/**
 * Given a string, find the length of the longest substring without repeating characters.
 *
 * Example 1:
 *
 * Input: "abcabcbb"
 * Output: 3
 * Explanation: The answer is "abc", with the length of 3.
 * Example 2:
 *
 * Input: "bbbbb"
 * Output: 1
 * Explanation: The answer is "b", with the length of 1.
 * Example 3:
 *
 * Input: "pwwkew"
 * Output: 3
 * Explanation: The answer is "wke", with the length of 3.
 * Note that the answer must be a substring, "pwke" is a Subsequence and NOT a Substring.
 *
 * Solution:
 * Approach 2: Sliding Window
 * Algorithm
 *
 * The naive approach is very straightforward. But it is too slow. So how can we optimize it?
 *
 * In the naive approaches, we repeatedly check a substring to see if it has duplicate character.
 * But it is unnecessary. If a substring s_{ij}s  from index i to j - 1 is already checked to have no duplicate characters.
 * We only need to check if s[j] is already in the substring s_{ij}.
 *
 * To check if a character is already in the substring, we can scan the substring, which leads to an O(n^2)algorithm.
 * But we can do better.
 *
 * By using HashSet as a sliding window, checking if a character in the current can be done in O(1).
 *
 * A sliding window is an abstract concept commonly used in array/string problems.
 * A window is a range of elements in the array/string which usually defined by the start and end indices, i.e.
 * [i, j)(left-closed, right-open). A sliding window is a window "slides" its two boundaries to the certain direction.
 * For example, if we slide [i, j) to the right by 1 element, then it becomes [i+1, j+1)(left-closed, right-open).
 *
 * Back to our problem. We use HashSet to store the characters in current window [i, j) (j = i initially).
 * Then we slide the index j to the right. If it is not in the HashSet, we slide j further.
 * Doing so until reach end of the string ( and if s[j] is already in the HashSet  ).
 *
 * At this point, we found the maximum size of substrings without duplicate characters start with index i.
 * If we do this for all i, we get our answer.
* */

public class LongestSubstringWithoutRepeatingCharacters {

    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        Set<Character> set = new HashSet<>();
        int j = 0;
        int ans = 0;
        int i = 0;
        while (i < n && j < n) {
            // try to extend the range [i, j]
            if (!set.contains(s.charAt(j))){
                set.add(s.charAt(j++));//slide to the right, open or expand window
                ans = Math.max(ans, j - i);
            }
            else {
                set.remove(s.charAt(i++));//slide left, closing or contract window
            }
        }
        return ans;
    }
    public static void main(String[] args){
        LongestSubstringWithoutRepeatingCharacters lswrc = new LongestSubstringWithoutRepeatingCharacters();
        String s1 = "abcabcbb"; //Expected output: 3
        String s2 = "bbbbb"; //Expected output: 1
        String s3 = "pwwkew"; //Expected output: 3

        System.out.println("Longest Substring Length without Repeating Characters for " + s1 + "'");
        System.out.println("            is =  " + lswrc.lengthOfLongestSubstring(s1) );

        System.out.println("Longest Substring Length without Repeating Characters for " + s2 + "'");
        System.out.println("            is =  " + lswrc.lengthOfLongestSubstring(s2) );

        System.out.println("Longest Substring Length without Repeating Characters for " + s3 + "'");
        System.out.println("            is = " + lswrc.lengthOfLongestSubstring(s3) );
    }
}
