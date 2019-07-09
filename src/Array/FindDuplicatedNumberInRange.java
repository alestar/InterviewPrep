package Array;

/**
 * Created by Alestar on 1/16/2019.
 */
public class FindDuplicatedNumberInRange {

    public static int Solution(int[] numbers) {
        for (int i = 1; i < numbers.length; i++) {
            boolean hasBeenSeen = false;
            int needle= numbers[i];
            for (int number : numbers) {

                System.out.println("    Current needle = " + needle  );
                System.out.println("    Current number is  = " + number  );
                if (number == needle) {

                    if (hasBeenSeen) {
                        return number;
                    } else {
                        hasBeenSeen = true;
                    }
                }
            }
        }

        // whoops--no duplicate
        throw new IllegalArgumentException("no duplicate!");
    }

    public static int findRepeatOrig(int[] theArray) {

        int floor = 1;
        int ceiling = theArray.length - 1;

        while (floor < ceiling) {
            System.out.println("    <floor> = " + floor  );
            System.out.println("    <ceiling> = " + ceiling  );

            // divide our range 1..n into an upper range and lower range
            // (such that they don't overlap)
            // lower range is floor..midpoint
            // upper range is midpoint+1..ceiling
            int midpoint = floor + ((ceiling - floor) / 2);
            int lowerRangeFloor   = floor;
            int lowerRangeCeiling = midpoint;
            int upperRangeFloor   = midpoint + 1;
            int upperRangeCeiling = ceiling;

            System.out.println("    <lowerRangeFloor> = " + lowerRangeFloor  );
            System.out.println("    <lowerRangeCeiling> = " + lowerRangeCeiling  );
            System.out.println("    <upperRangeFloor> = " + upperRangeFloor  );
            System.out.println("    <upperRangeCeiling> = " + upperRangeCeiling  );

            // count number of items in lower range
            int itemsInLowerRange = 0;
            for (int item : theArray) {
                System.out.println("            Looking at item = " + item );
                // is it in the lower range?
                if (item >= lowerRangeFloor && item <= lowerRangeCeiling) {
                    itemsInLowerRange += 1;
                }
            }
            System.out.println("        <itemsInLowerRange> = " + itemsInLowerRange  );
            int distinctPossibleIntegersInLowerRange = lowerRangeCeiling - lowerRangeFloor + 1;
            System.out.println("        <distinctPossibleIntegersInLowerRange> = " + distinctPossibleIntegersInLowerRange  );

            if (itemsInLowerRange > distinctPossibleIntegersInLowerRange) {

                // there must be a duplicate in the lower range
                // so use the same approach iteratively on that range
                floor   = lowerRangeFloor;
                ceiling = lowerRangeCeiling;
            } else {

                // there must be a duplicate in the upper range
                // so use the same approach iteratively on that range
                floor   = upperRangeFloor;
                ceiling = upperRangeCeiling;
            }
        }

        // floor and ceiling have converged
        // we found a number that repeats!
        return floor;
    }

    public static void printRepeating(int arr[]){
        int i;
        //System.out.println("The repeating elements are : ");

        for (i = 0; i < arr.length; i++)
        {   System.out.println("    Value at [" + i +"] = : " + arr[i]);
            System.out.println("    Value at Math.abs (" + arr[i] +") = : " + arr[Math.abs(arr[i])]);
            if (arr[Math.abs(arr[i])] >= 0)
                arr[Math.abs(arr[i])] = -arr[Math.abs(arr[i])];
            else {
                System.out.println(" Found duplicate = " + Math.abs(arr[i]));
            }
        }
    }

    public static void main(String[] args) {
        int[] arr= {6,6,7,8,9,10,1,2,3,4,5};
        int dup = findRepeatOrig(arr);
        System.out.println(" The duplicated number is = " + dup );
        //printRepeating(arr);
    }
}
