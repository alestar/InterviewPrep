package MyJava.Algorithms.Search;

/**
 * Created by Alestar on 1/14/2019.
 *
 * if k = log n
 *
 * where k = numbers of times required to multiply 1 by 'base'(i.e '2') until is equal to n
 * or k = numbers of times required to divide by 'base'(i.e '2') until is equal to 1
 */
public class BinarySearch {

    public static boolean binarySearch(int target, int[] nums) {
        // see if target appears in nums

        // we think of floorIndex and ceilingIndex as "walls" around
        // the possible positions of our target, so by -1 below we mean
        // to start our wall "to the left" of the 0th index
        // (we *don't* mean "the getLast index")
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


    private static boolean binarySearchIter(int[] array, int x) {
        int left =0;
        int right = array.length -1;

        while(left <= right) {
            int mid = left + ((right - left) / 2);//use this form to prevent overflow
            if (array[mid] == x) {
                return true;
            } else if (x < array[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return false;
    }

    private static boolean binarySearchRecursv(int[] array, int x, int left, int right) {

        if (left > right) {
            return false;
        }
        int mid = left + ((right -left) / 2);//use this form to prevent overflow

        if (array[mid] == x) {
            return true;
        } else if (x < array[mid]){
            return binarySearchRecursv(array, x, left, mid - 1);
        }else{
            return binarySearchRecursv(array, x, mid +1,right);
        }

    }

    public static boolean binarySearchRecursv(int[] array , int x){
        return binarySearchRecursv(array, x, 0, array.length -1);
    }

    public static void main(String[] args) {

    }

}
