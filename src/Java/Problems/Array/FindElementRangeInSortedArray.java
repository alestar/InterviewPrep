package Java.Problems.Array;

import java.util.Arrays;

/**
 * Given a sorted Array of int numbers:
 * Find the range of indices that include the target number
 * For example:
 * arr = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
 * x = 9
 * return  [6, 8], since x =9 is between index 6 and 8.
 */

public class FindElementRangeInSortedArray {

    public static int[] getRangeRecurv(int[] arr, int target){
        int first = binarySearchRecurv(target, arr, 0, arr.length -1, true);
        int last = binarySearchRecurv(target, arr, 0, arr.length -1, false);
        return new int[]{first,last};
    }

    public static int[] getRangeIter(int[] arr, int target){
        int first = binarySearchIter(target, arr, 0, arr.length -1, true);
        int last = binarySearchIter(target, arr, 0, arr.length -1, false);
        return new int[]{first,last};
    }

    private static int binarySearchRecurv(int target, int[] arr, int l, int h, boolean findFirst) {
        if(h < l)
            return -1;
        int m = l + (h - l) / 2;
        if(findFirst){
            if(m == 0 || ( arr[m] == target && target > arr[m - 1] )){
                return m;
            }
            if(target > arr[m] ){
                return binarySearchRecurv(target,arr, m + 1, h, findFirst);
            }
            else{
                return  binarySearchRecurv(target,arr, l, m - 1, findFirst);
            }
        }
        else{
            if(m == 0 || ( arr[m] == target && target < arr[m + 1] )){
                return m;
            }
            if (target < arr[m]) {
                return binarySearchRecurv(target, arr, l, m - 1, findFirst);
            }
            else{
                 return  binarySearchRecurv(target, arr, m + 1, h, findFirst);
            }
        }
    }

    private static int binarySearchIter(int target, int[] arr, int l, int h, boolean findFirst) {
        while(true) {
            if (h < l)
                return -1;
            int m = l + (h - l) / 2;
            if (findFirst) {
                if (m == 0 || (arr[m] == target && target > arr[m - 1])) {
                    return m;
                }
                if (target > arr[m]) {
                    l= m + 1;
                } else {
                    h = m - 1;
                }
            } else {
                if (m == 0 || (arr[m] == target && target < arr[m + 1])) {
                    return m;
                }
                if (target < arr[m]) {
                    h = m - 1;
                } else {
                    l= m + 1;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, 3, 5, 7, 8, 9, 9, 9, 15};
        int target =9; // Expected [6, 8]

        System.out.println("Using Recursion: The range of index for the target = " + target + " is: " + Arrays.toString(getRangeRecurv(arr,target)));
        System.out.println("Using Iteration: The range of index for the target = " + target + " is: " + Arrays.toString(getRangeIter(arr,target)));
    }
}
