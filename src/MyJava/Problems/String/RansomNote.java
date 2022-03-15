package MyJava.Problems.String;

import java.util.HashMap;
import java.util.Map;

/**
 * Verify if a ransom note can be created from a magazine.
 * The magazine most have all the words required to complete the note and the necessary amount for repeated words.
 */

public class RansomNote {

    private static HashMap<String, Integer> getStringFreq(String[] text) {

        HashMap<String, Integer> frequencies = new HashMap<>();
        for (String word: text) {
            if(!frequencies.containsKey(word)){
                frequencies.put(word,0);
            }
            frequencies.put(word,frequencies.get(word) + 1);
        }
        return frequencies;
    }

    private static Boolean hasEnoughStrings(HashMap<String, Integer> magazineFreq, HashMap<String, Integer> noteFreq) {

        for (Map.Entry<String, Integer> entry: noteFreq.entrySet()) {
            String word = entry.getKey();
            if(!magazineFreq.containsKey(word)|| magazineFreq.get(word) < entry.getValue()){
                return false;
            }
        }
        return true;
    }


    private static Boolean canBuildRansomNote(String[] magazine, String[] note) {
        HashMap<String, Integer> magazineFreq = getStringFreq(magazine);
        HashMap<String, Integer> noteFreq = getStringFreq(note);
        return hasEnoughStrings(magazineFreq, noteFreq);
    }



    public static void main(String[] args) {
        String[] magazine1 = {"hello", "world", "blah"};
        String[] note1 = {"hello", "world", "world"};
        System.out.println("Can build Ransom Note (1): " + canBuildRansomNote(magazine1, note1));

        String[] magazine2 = {"hello", "world", "world","hi"};
        String[] note2 = {"hello", "world", "world"};
        System.out.println("Can build Ransom Note (2): " + canBuildRansomNote(magazine2, note2));
    }


}
