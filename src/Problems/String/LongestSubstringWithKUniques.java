package Problems.String;

import java.util.HashSet;
import java.util.Set;

/**
 *Given a string, find the length of the longest substring in it with no more than K distinct characters.
 *
 * Example 1:
 *
 * Input: String="araaci", K=2
 * Output: 4
 * Explanation: The longest substring with no more than '2' distinct characters is "araa".
 *
 *  *
 *  * Example 1:
 *  *
 *  * Input: String="zearaaci", K=2
 *  * Output: 4
 *  * Explanation: The longest substring with no more than '2' distinct characters is "araa".
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

public class LongestSubstringWithKUniques {

    public static final int CHAR_RANGE = 128;

    /*
    public String LongestSubstringWithKUniques(String s, int k) {//"araaci",
        int n = s.length();
        HashMap<Character, Integer> map = new HashMap<>();
        int  start = 0, end = 0, unique =0;
        String temp="";
        String max="";
        for (int i = 0; i <n ; i++) {
            if (!map.containsKey(s.charAt(i))) {//New element
                map.put(s.charAt(i),1);//Add to map with count = 1

                if (unique < k) {// And is under K unique elements,
                    map.put(s.charAt(i), 1);// Then slide right, open or expand window
                    end++;
                    unique++;

                    //Update max
                    max = updateMaxString(s, start, end, max);
                }
                else {
                    map.put(s.charAt(start), map.get(s.charAt(start)) -1);// Decrease count of the element in map
                    start++; // Then slide left, closing or contract window

                    if(map.get(s.charAt(start)) == 0 )// If is the last of that element shifted away by the window, decrease the amount of unique
                        unique--;

                }
            }
            else {// A known element or previously observed
                map.put(s.charAt(i), map.get(s.charAt(i)) + 1);// Then slide right, open or expand window
                end++;
                //Update max
                if (map.get(s.charAt(i-1)) < 1 && unique < k && i> 0 )
                     max = updateMaxString(s, start, end, max);
            }

        }
        return max;
    }

    private String updateMaxString(String s, int start, int end, String max) {
        String temp;
        temp = s.substring(start, end);
        if (max.compareTo(temp) == -1) {
            max = temp;
        }
        return max;
    }
*/

    // Function to find longest substring of given string containing
    // k distinct characters using sliding window
    public static String longestSubstr(String str, int k)
    {
        // stores longest substring boundaries
        int end = 0, begin = 0;

        // set to store distinct characters in a window
        Set<Character> window = new HashSet<>();

        // count array to store frequency of characters present in
        // current window
        // we can also use a map instead of count array
        int[] freq = new int[CHAR_RANGE];

        // [low..high] maintain sliding window boundaries
        for (int low = 0, high = 0; high < str.length(); high++)
        {
            window.add(str.charAt(high));
            freq[str.charAt(high)]++;

            // if window size is more than k, remove characters from the left
            while (window.size() > k)
            {
                // if the frequency of leftmost character becomes 0 after
                // removing it in the window, remove it from set as well
                if (--freq[str.charAt(low)] == 0) {
                    window.remove(str.charAt(low));
                }
                low++;// reduce window size
            }

            // update maximum window size if necessary
            if (end - begin < high - low)
            {
                end = high;
                begin = low;
            }
        }

        // return longest substring found at str[begin..end]
        return str.substring(begin, end + 1);
    }


    public static void main(String[] args){
        LongestSubstringWithKUniques kUniques = new LongestSubstringWithKUniques();
        String s0 = "araaci"; //Expected output: 'araa'
        int k0=2;

        String s1 = "aabbcc"; //Expected output: {"aa" , "bb" , "cc"}
        int k1 = 1;

        String s2 = "aabbcc"; //Expected output: {"aabb" , "bbcc"}
        int k2 = 2;

        String s3 = "abcbdbdbbdcdabd"; //Expected output: {"bdbdbbd" }
        int k3 = 2;
        int k4 = 3;

        String s4 = "aaabbb";//Expected output: 'aaabbb'
        int k5 = 3;

        String s6 = "araaciaraaaaaaaci"; //Expected output: 'araaaaaaa'
        int k6=2;

        System.out.println("Looking at 's0' = '" + s0 + "'");
        System.out.println("    with 'k0' = " + k0);
        //System.out.println("    has Longest Substring Length  =  " + kUniques.LongestSubstringWithKUniques(s0,k0) );
        System.out.println("    is (longestSubstr) = " + kUniques.longestSubstr(s0,k0));

        System.out.println("Looking at 's1' = '" + s1 + "'");
        System.out.println("    with 'k1' = " + k1);
        //System.out.println("    has Longest Substring Length  =  " + kUniques.LongestSubstringWithKUniques(s1,k1) );
        System.out.println("    and (longestSubstr) = " + kUniques.longestSubstr(s1,k1));

        System.out.println("Looking at 's2' = '" + s2 + "'");
        System.out.println("    with 'k2' = " + k2);
        //System.out.println("    has Longest Substring Length  =  " + kUniques.LongestSubstringWithKUniques(s2,k2) );
        System.out.println("    and (longestSubstr) = " + kUniques.longestSubstr(s2,k2));


        System.out.println("Looking at 's3' = '" + s3 + "'");
        System.out.println("    with 'k3' = " + k3);
       //System.out.println("    has Longest Substring Length  =  " + kUniques.LongestSubstringWithKUniques(s3,k3) );
        System.out.println("    and (longestSubstr) = " + kUniques.longestSubstr(s3,k3));

        System.out.println("Looking at 's6' = '" + s6 + "'");
        System.out.println("    with 'k4' = " + k4);
        //System.out.println("    has Longest Substring Length  =  " + kUniques.LongestSubstringWithKUniques(s6,k4) );
        System.out.println("    and (longestSubstr) = " + kUniques.longestSubstr(s6,k4));

        System.out.println("Looking at 's3' = '" + s4 + "'");
        System.out.println("    with 'k4' = " + k5);
        //System.out.println("    has Longest Substring Length  =  " + kUniques.LongestSubstringWithKUniques(s4,k5) );
        System.out.println("    and (longestSubstr) = " + kUniques.longestSubstr(s4,k5));

        System.out.println("Looking at 's6' = '" + s4 + "'");
        System.out.println("    with 'k6' = " + k6);
        //System.out.println("    has Longest Substring Length  =  " + kUniques.LongestSubstringWithKUniques(s6,k6) );
        System.out.println("    and (longestSubstr) = " + kUniques.longestSubstr(s6,k6));

    }
}
