/**
 * Created by Alestar on 1/14/2019.
 */
public class BinarySearch {

    public static boolean binarySearch(int target, int[] nums) {
        // see if target appears in nums

        // we think of floorIndex and ceilingIndex as "walls" around
        // the possible positions of our target, so by -1 below we mean
        // to start our wall "to the left" of the 0th index
        // (we *don't* mean "the last index")
        int floorIndex = -1;
        int ceilingIndex = nums.length;

        // if there isn't at least 1 index between floor and ceiling,
        // we've run out of guesses and the number must not be present
        while (floorIndex + 1 < ceilingIndex) {

            // find the index ~halfway between the floor and ceiling
            // we use integer division, so we'll never get a "half index"
            int distance = ceilingIndex - floorIndex;
            int halfDistance = distance / 2;
            int guessIndex = floorIndex + halfDistance;

            int guessValue = nums[guessIndex];

            if (guessValue == target) {
                return true;
            }

            if (guessValue > target) {

                // target is to the left, so move ceiling to the left
                ceilingIndex = guessIndex;

            } else {

                // target is to the right, so move floor to the right
                floorIndex = guessIndex;
            }
        }

        return false;
    }

}
