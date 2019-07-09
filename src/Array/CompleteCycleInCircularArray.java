package Array; /**
 * Created by Alestar on 1/29/2019.
 */

/**
 * Given a circular array of relative indices, find out if there is a complete cycle. Each cell
 * points relatively to another cell (e.g., -1 to the previous cell, 2 to the second next cell and 0
 * to the same cell). A complete cycle corresponds to visiting all the cells, only once each.
 *
 * Example:
 *   [2, 2, -1] --> true
 *   [2, 2, 0] --> false
 *   [0] --> true
 *   [1, -1] --> true
 *
 */
public class CompleteCycleInCircularArray {

    /**
     * Let n = length(arr).
     * Time complexity:  O(n)
     * Space complexity: O(1)
     */
    public static boolean Solution(int[] arr) {
        final int n = arr.length;
        int index = 0;  // starting index, the value does not matter if there is indeed a complete cycle
        for(int i = 0; i < n; i++) {  // at most n steps
            // in Java, -b < a % b < b but 0 < (a % b + b) % b < b
            index = ((index + arr[index]) % n + n) % n;
            if(index == 0 && i < n - 1) {  // subcyle
                return false;
            }
        }
        return index == 0;  // are we back to the original cell after n steps
    }
    public static boolean hasCycle(int[] arr) {
        final int n = arr.length;
        int currentPos = 0;  // starting pos, the value does not matter if there is indeed a complete cycle
        for(int i = 0; i < n; i++) {  // at most n steps
            currentPos = ((currentPos + arr[currentPos])) % n;
            if(currentPos == 0 && i < n - 1) {  // subcyle
                return false;
            }
        }
        return currentPos == 0;  // are we back to the original cell after n steps
    }

    public static void main(String[] args) {

        int[] input1 = {2,2,-1};// true
        int[] input2 = {2,2,0}; // false (not a cycle)
        int[] input3 = {0};     // true
        int[] input4 = {1,-1};  // true
        int[] input5 ={2, -1, 1, 2, 2};// false (cycle but not complete)

        System.out.println("The arr {2,2,-1} is complete and a cycle? " +  hasCycle(input1));
        System.out.println("The arr {2,2,0} is complete and  a cycle? " +  hasCycle(input2));
        System.out.println("The arr {0} is complete and a cycle? " +  hasCycle(input3));
        System.out.println("The arr {1,-1} is complete and a cycle? " +  hasCycle(input4));
        System.out.println("The arr {2, -1, 1, 2, 2} is complete and  a cycle? " +  hasCycle(input5));
    }
}
