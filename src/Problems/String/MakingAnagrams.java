package Problems.String;

/**
 *
 * @author : Alestar
 *
 * Given two Strings (lowercase a->z), how many characters do we need to remove (from either) to make them anagrams?
 * Anagrams: Are permutations or rearrangements of the words
 *
 * Return number of character that need to change
 *
 * Example: hello, billion -> Answer: = 6 ('he' from 'hello' and 'biin' from 'billion')
 * Example: glue, legs -> Answer =  2 ('u' from 'glue' and 's' from 'legs')
 * Example: candy, day -> Answer = 2 ('cn' from 'candy')
 *
 * */

public class MakingAnagrams {

    public static int NUMBER_LETTERS = 26;


    public int numberNeeded (String first, String second){
        
        int [] charCount1 =  getCharCount(first);
        int [] charCount2 =  getCharCount(second);
        return getDelta(charCount1,charCount2);
    }

    private static int[] getCharCount(String s) {
        int[] charCounts = new int [NUMBER_LETTERS];
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int offset = (int) 'a'; // Any letter/number - 'a' give us the index in the array with out the offset of ASCII

            int code = c - offset;
            charCounts[code]++;
        }
        return charCounts;
    }

    public static int getDelta(int[] countArr1, int[] countArr2){
        if(countArr1.length != countArr2.length){
            return -1;
        }
        int delta = 0;
        for (int i = 0; i < countArr1.length; i++) {
            int diff = Math.abs(countArr1[i] - countArr2[i]);
            delta += diff;
        }
        return delta;

    }

    public static void main(String[] args) {

        MakingAnagrams ma = new MakingAnagrams();

        String s1 = "hello";
        String s2 = "billion";

        String s3 = "glue";
        String s4 = "legs";

        String s5 = "candy";
        String s6 = "day";

        System.out.println("Calculating diff to make Anagrams: ");
        System.out.println("    with 's1': " + s1);
        System.out.println("    with 's2': " + s2);
        System.out.println("    = " + ma.numberNeeded(s1,s2));

        System.out.println("Calculating diff to make Anagrams: ");
        System.out.println("    with 's3': " + s3);
        System.out.println("    with 's4': " + s4);
        System.out.println("    = " + ma.numberNeeded(s3,s4));

        System.out.println("Calculating diff to make Anagrams: ");
        System.out.println("    with 's5': " + s5);
        System.out.println("    with 's6': " + s6);
        System.out.println("    = " + ma.numberNeeded(s5,s6));
    }
}
