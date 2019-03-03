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

        System.out.println("    All chars except last one: " +  allCharsExceptLast);
        char lastChar = inputString.charAt(inputString.length() - 1);
        System.out.println("    last char: " +  lastChar);

        // recursive call: get all possible permutations for all chars except last
        Set<String> permutationsOfAllCharsExceptLast = getPermutations(allCharsExceptLast);

        // put the last char in all possible positions for each of the above permutations
        Set<String> permutations = new HashSet<>();
        for (String currentPermutationOfAllCharsExceptLast : permutationsOfAllCharsExceptLast) {
            for (int position = 0; position <= allCharsExceptLast.length(); position++) {

                String permutation = currentPermutationOfAllCharsExceptLast.substring(0, position) + lastChar
                        + currentPermutationOfAllCharsExceptLast.substring(position);
                System.out.println("        New permutation: {'" +  permutation + "'}");
                System.out.println("            Permutations Of All Chars Except Last: " +  permutationsOfAllCharsExceptLast + " , with size: [" +  permutationsOfAllCharsExceptLast.size() + "]");
                System.out.println("            All chars except last one: '" +  allCharsExceptLast + "' ,with length: (" +  allCharsExceptLast.length() + ")");
                System.out.println("                Current Item : '" +  currentPermutationOfAllCharsExceptLast + "'");
                System.out.println("                    Current Position : " +  position);
                System.out.println("                    First part : " +  currentPermutationOfAllCharsExceptLast.substring(0, position));
                System.out.println("                    + last char: " +  lastChar);
                System.out.println("                    + last part: " +  currentPermutationOfAllCharsExceptLast.substring(position));

                permutations.add(permutation);
            }
        }

        return permutations;
    }
    public static void main(String[] args) {

        Set<String> perm= getPermutations("cats");
        System.out.println("All the permutations: " +  perm);

    }
}
