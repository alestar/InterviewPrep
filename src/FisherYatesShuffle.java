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

    public static void Solution(int[] theArray) {

        // if it's 1 or 0 items, just return
        if (theArray.length <= 1) {
            return;
        }

        // walk through from beginning to end
        for (int indexWeAreChoosingFor = 0;
             indexWeAreChoosingFor < theArray.length - 1; indexWeAreChoosingFor++) {

            // choose a random not-yet-placed item to place there
            // (could also be the item currently in that spot)
            // must be an item AFTER the current item, because the stuff
            // before has all already been placed
            int randomChoiceIndex = getRandom(indexWeAreChoosingFor, theArray.length - 1);

            // place our random choice in the spot by swapping
            if (randomChoiceIndex != indexWeAreChoosingFor) {
                int valueAtIndexWeChoseFor = theArray[indexWeAreChoosingFor];
                theArray[indexWeAreChoosingFor] = theArray[randomChoiceIndex];
                theArray[randomChoiceIndex] = valueAtIndexWeChoseFor;
            }
        }
    }

    public static void main(String[] args) {

        int[] arrayOfInts = new int[]{6,7,18,44,5,5,12,3};
        System.out.println("Array before shuffle = " + Arrays.toString(arrayOfInts));
        Solution(arrayOfInts);
        System.out.println("Array after shuffle = " + Arrays.toString(arrayOfInts));
    }


}
