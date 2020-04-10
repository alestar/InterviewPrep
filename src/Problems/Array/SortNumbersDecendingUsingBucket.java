package Problems.Array;

import java.util.Arrays;

/**
 * Created by Alestar on 1/16/2019.
 */
public class SortNumbersDecendingUsingBucket {

    public static int[] sortScores(int[] unorderedScores, int highestPossibleScore) {

        // array of 0s at indices 0..highestPossibleScore
        int[] scoreCounts = new int[highestPossibleScore + 1];

        // populate scoreCounts
        for (int score : unorderedScores) {
            scoreCounts[score]++;
        }

        // populate the final sorted array
        int[] sortedScores = new int[unorderedScores.length];
        int currentSortedIndex = 0;

        // for each item in scoreCounts
        for (int score = highestPossibleScore; score >= 0; score--) {
            int count = scoreCounts[score];

            // for the number of times the item occurs
            for (int occurrence = 0; occurrence < count; occurrence++) {

                // add it to the sorted array
                sortedScores[currentSortedIndex] = score;
                currentSortedIndex++;
            }
        }

        return sortedScores;
    }
    public static void main(String[] args) {

        int[] unsortedScores = {37, 89, 41, 65, 91, 53};// sortedScores: [91, 89, 65, 53, 41, 37]
        final int HIGHEST_POSSIBLE_SCORE = 100;
        int[] sortedScores = sortScores(unsortedScores, HIGHEST_POSSIBLE_SCORE);
        System.out.println(" The sorted scores are : " + Arrays.toString(sortedScores));
    }
}
