package MyJava.Problems.Array;

import java.util.Arrays;
import java.util.Random;

/**
 * Created by Alestar on 1/14/2019.
 */
public class FisherYatesShuffle {

    private static Random rand = new Random();

    private static int getRandom(int floor, int ceiling) {
        return rand.nextInt((ceiling - floor) + 1) + floor;
    }

    public static void Solution(int[] arr) {

        int n=arr.length;
        // if it's 1 or 0 items, just return
        if (n<= 1) {
            return;
        }

        // walk through from beginning to end
        for (int i = 0; i < n - 1; i++) {

            // pick a random not-yet-placed item to place there
            // (could also be the item currently in that spot)
            // must be an item AFTER the current item, because the stuff
            // before has all already been placed
            int pick = getRandom(i, n - 1);

            // place our random choice in the spot by swapping
            if (pick != i) {
                int temp = arr[i];
                arr[i] = arr[pick];
                arr[pick] = temp;
            }
        }
    }

    public static void main(String[] args) {

        int[] arr = new int[]{6,7,18,44,5,5,12,3};
        System.out.println("Java.Problems.Array before shuffle = " + Arrays.toString(arr));
        Solution(arr);
        System.out.println("Java.Problems.Array after shuffle = " + Arrays.toString(arr));
    }


}
