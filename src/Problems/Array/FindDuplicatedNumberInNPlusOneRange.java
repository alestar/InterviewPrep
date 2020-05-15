package Problems.Array;

import java.util.Arrays;
import java.util.HashSet;


/**
 * Created by Alestar on 1/16/2019.
 *
 * Find Duplicate Number
 *
 * Given an arrays nums containing n+1 integers where each integer is between 1 and n (inclusive).
 * Prove that at least one duplicate number must exist.
 * Assume that there is only one repeated number, but it could be repeated more than one. i.e:
 * nums = [2,2,1,3,2,5,6]
 * nums = [6,4,1,1,2,1,1]
 *
 * Requirements:
 * You must use only constant, O(1) extra space.
 * You ust not modify the array (assume the array is read only)
 * Your runtime complexity should be less than O(n2), BUT ideally O(n).
 *
 * Observation:
 * Think about the original problem statement. We know that we have at least one repeat because there are n+1 items and they are all in the range 1..n,
 * which contains only n distinct integers.
 *
 * This notion of "we have more items than we have possibilities, so we must have at least one repeat" is pretty powerful.
 * It's sometimes called the pigeonhole principle:
 *
 * The pigeonhole principle states that if n items are put into m containers, with n > m, then at least one container must contain more than one item. *
 * For example, there must be at least two left gloves or two right gloves in a group of three gloves.
 */
public class FindDuplicatedNumberInNPlusOneRange {

    /**
    * This is the Naive Solution and it's time complexity is O(n^2)
    */
    public static int findNaive(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            boolean hasBeenSeen = false;
            int needle= nums[i];
            for (int number : nums) {

                System.out.println("    Current needle = " + needle  );
                System.out.println("    Current number is  = " + number  );
                if (number == needle) {

                    if (hasBeenSeen) {
                        System.out.println("The duplicated number using 'findUsingSort' ");
                        System.out.println("    with nums [] array  = " + Arrays.toString(nums));
                        System.out.println("     is = " + number);
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

    /**
     * Another less Naive but straight forward Solution is to sort the array.
     * Which it's runtime complexity is O(n logn); but is not O(n).
     */
    public static int findUsingSort(int[] nums){
       Arrays.sort(nums);
        for (int i=0; i<nums.length; i++) {
            if(nums[i] == nums[i+1]) {
                System.out.println("The duplicated number using 'findUsingSort' ");
                System.out.println("    with nums [] array  = " + Arrays.toString(nums));
                System.out.println("     is = " + nums[i]);
                return nums[i];
            }
        }

        return -1;
    }

    /**
     * This is another similar runtime complexity solution is.
     * The space complexity is O(1) because no additional data structures is being used, only pointers.
     * However runtime complexity is O(n logn). We are splitting the search in half every time.
     */
    public static int findUsingBinarySearch(int[] nums) {

        int floor = 1;
        int ceiling = nums.length - 1;

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
            for (int item : nums) {
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
        System.out.println("The duplicated number using 'findUsingBinarySearch' ");
        System.out.println("    with nums [] array  = " + Arrays.toString(nums));
        System.out.println("     is = " + floor);
        return floor;
    }

    /**
     * Find and print repeated
     * @param nums
     */
    public static void findPrintRepeating(int nums[]){
        int i;
        //System.out.println("The repeating elements are : ");

        for (i = 0; i < nums.length; i++)
        {   System.out.println("    Value at [" + i +"] = : " + nums[i]);
            System.out.println("    Value at Problems.Math.abs (" + nums[i] +") = : " + nums[Math.abs(nums[i])]);
            if (nums[Math.abs(nums[i])] >= 0)
                nums[Math.abs(nums[i])] = -nums[Math.abs(nums[i])];
            else {
                System.out.println(" Found duplicate = " + Math.abs(nums[i]));
            }
        }
    }

    /**
     * Another Solution is to use a hash set (Hash map is not necessary since we are only using one dimension).
     * This is a better Solution , with runtime complexity O(n),
     * because worst case, the duplicate elements are at the end of the array.
     * However space complexity O(n). The map may hold all the elements of the array, in the worst case.
     * This is a classic example of trading space complexity cost for the sake of improving time complexity cost.
     */
    public static int findUsingHashSet(int[] nums){
        HashSet<Integer> seen = new HashSet<>();

        for (int i=0; i<nums.length; i++) {
            if (seen.contains(nums[i])) {
                System.out.println("The duplicated number using 'findUsingHashSet' ");
                System.out.println("    with nums [] array  = " + Arrays.toString(nums));
                System.out.println("     is = " + nums[i]);
                return nums[i];
            }
            seen.add(nums[i]);
        }
        return -1;
    }


    /**
     * This is an optimal Solution with runtime complexity O(n) and space complexity O(1),
     * because no additional data structures is being used, only pointers.
     * and at the worst case duplicate elements are at the end of the array.
     *
     * This solution, solve the problem in linear runtime and constant space.
     * It is a cycle detection algorithm, where one pointer (the hare) traverses twice as fast as the other pointer.
     * Once the pointers meet you can trace back where the cycle begin.
     * In this case, the values of the Arrays are use as the "pointers" in the array, similar to nodes in a linked list.
     * Because each number is from 1 to n, then each value will have to point a valid index.
     * And since there is a duplicate number, there will be a cycle.
     * The answer is where that cycle start
     */
    public static int findUsingFloydsTortoiseAndHare(int[] nums) {

        System.out.println("Finding duplicates using Floyds's tortoise and hare");

        int hare=nums[0];
        int tortoise=nums[0];
        System.out.println("    The 'tortoise' start at = " + tortoise);
        System.out.println("    The 'hare' start at = " + hare);
        while (true) {
            tortoise = nums[tortoise];
            hare= nums[nums[hare]];
            System.out.println("    The 'tortoise' value is = " + tortoise);
            System.out.println("    The 'hare' value is = " + hare);
            if(tortoise == hare)
                break;
        }
        System.out.println("The 'tortoise' exit at value = " + tortoise);

        int ptr1 = nums[0];
        int ptr2 =  tortoise;

        System.out.println("    The 'ptr1' value = " + ptr1);
        System.out.println("    The 'ptr2' value = " + ptr2);
        while (ptr1 != ptr2){// This second loop is to found where the cycle begins in the array
            ptr1= nums[ptr1];
            ptr2= nums[ptr2];
            System.out.println("    The 'ptr1' value = " + ptr1);
            System.out.println("    The 'ptr2' value = " + ptr2);
        }

        System.out.println("The duplicated number using 'findUsingFloydsTortoiseAndHare' ");
        System.out.println("    with nums [] array  = " + Arrays.toString(nums));
        System.out.println("     is = " + ptr1);
        System.out.println();
        return ptr1;
    }


    public static void main(String[] args) {
        int[] nums= {6,6,7,8,9,10,1,2,3,4,5};
        int[] nums1= {2,2,1,3,2,5,6};
        int[] nums2= {6,4,1,1,2,1,1};

      /*  findNaive(nums);
        findNaive(nums1);
        findNaive(nums2);

        findUsingSort(nums);
        findUsingSort(nums1);
        findUsingSort(nums2);

        findUsingBinarySearch(nums);
        findUsingBinarySearch(nums1);
        findUsingBinarySearch(nums2);

        findUsingHashSet(nums);
        findUsingHashSet(nums1);
        findUsingHashSet(nums2);*/

        findUsingFloydsTortoiseAndHare(nums);
        findUsingFloydsTortoiseAndHare(nums1);
        findUsingFloydsTortoiseAndHare(nums2);

    }
}
