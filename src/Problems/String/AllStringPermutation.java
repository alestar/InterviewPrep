package Problems.String;

import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

/**
 * Created by Alestar on 1/27/2019.
 */
public class AllStringPermutation {


    public static Set<String> getPermutations(String inputString) {

        // base case
        if (inputString.length() <= 1) {
            return new HashSet<>(Collections.singletonList(inputString));
        }
        String allCharsExceptLast = inputString.substring(0, inputString.length() - 1);

        System.out.println("    All chars except getLast one: " +  allCharsExceptLast);
        char lastChar = inputString.charAt(inputString.length() - 1);
        System.out.println("    getLast char: " +  lastChar);

        // recursive call: get all possible permutations for all chars except getLast
        Set<String> permutationsOfAllCharsExceptLast = getPermutations(allCharsExceptLast);

        // put the getLast char in all possible positions for each of the above permutations
        Set<String> permutations = new HashSet<>();
        for (String currentPermutationOfAllCharsExceptLast : permutationsOfAllCharsExceptLast) {
            for (int position = 0; position <= allCharsExceptLast.length(); position++) {

                String permutation = currentPermutationOfAllCharsExceptLast.substring(0, position) + lastChar
                        + currentPermutationOfAllCharsExceptLast.substring(position);
                System.out.println("        New permutation: {'" +  permutation + "'}");
                System.out.println("            Permutations Of All Chars Except Last: " +  permutationsOfAllCharsExceptLast + " , with size: [" +  permutationsOfAllCharsExceptLast.size() + "]");
                System.out.println("            All chars except getLast one: '" +  allCharsExceptLast + "' ,with length: (" +  allCharsExceptLast.length() + ")");
                System.out.println("                Current Item : '" +  currentPermutationOfAllCharsExceptLast + "'");
                System.out.println("                    Current Position : " +  position);
                System.out.println("                    First part : " +  currentPermutationOfAllCharsExceptLast.substring(0, position));
                System.out.println("                    + getLast char: " +  lastChar);
                System.out.println("                    + getLast part: " +  currentPermutationOfAllCharsExceptLast.substring(position));

                permutations.add(permutation);
            }
        }

        return permutations;
    }
    public static void main(String[] args) {

        Set<String> perm= getPermutations("cats");
        System.out.println("All the permutations: " +  perm);

    }

    /**
     * Created by Alestar on 3/17/2019.
     */
    public static class LookAndSay {

        // Returns n'th term in
        // look-and-say sequence
        static String countnAndSayFor(int n){
            // Base cases
            if (n == 1)     return "1";
            if (n == 2)     return "11";

            // Find n'th term by generating
            // all terms from 3 to n-1.
            // Every term is generated
            // using previous term

            // Initialize previous term
            String str = "11";
            for (int i = 3; i <= n; i++)
            {
                // In below for loop, previous
                // character is processed in
                // current iteration. That is
                // why a dummy character is
                // added to make sure that loop
                // runs one extra iteration.
                str += '$';
                int len = str.length();

                int cnt = 1; // Initialize count
                // of matching chars
                String tmp = ""; // Initialize i'th
                // term in series
                char []arr = str.toCharArray();
                System.out.println("current 'tmp' = " + tmp);


                // Process previous term
                // to find the next term
                for (int j = 1; j < len; j++)
                {
                    // If current character
                    // does't match
                    System.out.println("current 'j' = " + j);
                    if (arr[j] != arr[j - 1])
                    {
                        // Append count of
                        // str[j-1] to temp
                        tmp += cnt + 0;
                        System.out.println("current 'tmp' after add 'cnt' = " + tmp);

                        // Append str[j-1]
                        tmp += arr[j - 1];
                        System.out.println("current 'tmp' after append 'str[j-1]' = " + tmp);

                        // Reset count
                        cnt = 1;
                    }

                    // If matches, then increment
                    // count of matching characters
                    else cnt++;
                    System.out.println("current 'cnt' = " + cnt);

                }

                // Update str
                str = tmp;
            }

            return str;
        }

        static String countAndSayWhile(int n) {
            if (n <= 0)
                return null;

            String result = "1";
            int i = 1;

            while (i < n) {
                StringBuilder sb = new StringBuilder();
                int count = 1;
                for (int j = 1; j < result.length(); j++) {
                    if (result.charAt(j) == result.charAt(j - 1)) {
                        count++;
                    } else {
                        sb.append(count);
                        sb.append(result.charAt(j - 1));
                        count = 1;
                    }
                }

                sb.append(count);
                sb.append(result.charAt(result.length() - 1));
                result = sb.toString();
                i++;
            }

            return result;
        }

        // Driver Code
        public static void main(String[] args){
            int N = 5;
            System.out.println("Input N = " + N );
            System.out.println("Count say using for loops = " + countnAndSayFor(N));
            System.out.println("Count say using while loops= " + countAndSayWhile(N));
        }

    }
}
