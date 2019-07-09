package String; /**
 * Created by Alestar on 3/18/2019.
 */

/**
    Inserting one character anywhere in the word (including at the beginning and end)
    Removing one character
    Replacing one character
 */

public class EditDistanceOne {

    static boolean isEditDistanceOne(String s1, String s2) {
        // Find lengths of given strings
        int m = s1.length(), n = s2.length();

        // If difference between lengths is
        // more than 1, then strings can't
        // be at one distance
        if (Math.abs(m - n) > 1)
            return false;

        int count = 0; // Count of edits

        int i = 0, j = 0;
        while (i < m && j < n)
        {

            // If current characters don't match
            if (s1.charAt(i) != s2.charAt(j)) {
                if (count == 1)
                    return false;
                // Increment count of edits
                count++;
                // If length of one string is bigger, then only possible edit is to remove a character
                if (m > n)
                    i++;
                else if (m< n)
                    j++;
                else {// If lengths of both strings is the same
                    i++;
                    j++;
                }

            }
            else {// If current characters match
                i++;
                j++;
            }
        }

        // If there is an extra character in any string, after the loop exit because for the shortest one
        if (i < m || j < n)
            count++;//That's another edit (or difference) that needs to be counted

        return count == 1;
    }

    // driver code
    public static void main (String[] args)
    {
        /*
        OneEditApart("gfg", "gf") = true
        OneEditApart("cat", "dog") = false
        OneEditApart("cat", "cats") = true
        OneEditApart("cat", "cut") = true
        OneEditApart("cat", "cast") = true
        OneEditApart("cat", "at") = true
        OneEditApart("cat", "act") = false
        * */

        String s1 = "gfg";
        String s2 = "gf";

        String s3 = "cat";
        String s4 = "dog";

        String s5 = "cat";
        String s6 = "cats";

        String s7 = "cat";
        String s8 = "cut";

        String s9 = "cat";
        String s10 = "cast";

        String s11 = "cat";
        String s12 = "at";

        String s13 = "cat";
        String s14 = "act";

        System.out.println("OneEditApart('gfg', 'gf') = " + isEditDistanceOne(s1,s2));
        System.out.println("OneEditApart('cat', 'dog') = " + isEditDistanceOne(s3,s4));
        System.out.println("OneEditApart('cat', 'cats') = " + isEditDistanceOne(s5,s6));
        System.out.println("OneEditApart('cat', 'cut') = " + isEditDistanceOne(s7,s8));
        System.out.println("OneEditApart('cat', 'cast') = " + isEditDistanceOne(s9,s10));
        System.out.println("OneEditApart('cat', 'at') = " + isEditDistanceOne(s11,s12));
        System.out.println("OneEditApart('cat', 'act') = " + isEditDistanceOne(s13,s14));


    }

}
