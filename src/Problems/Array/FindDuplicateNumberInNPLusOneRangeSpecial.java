package Problems.Array;

import java.util.Arrays;

/**
 * Created by Alestar on 2/18/2019.
 *
 * In Find a duplicate, Space Edition™, we were given a list of integers where:
 *
 * the integers are in the range 1..n1..n
 * the list has a length of n+1n+1
 * These properties mean the list must have at least 1 duplicate. Our challenge was to find a duplicate number, while optimizing for space.
 * We used a divide and conquer approach, iteratively cutting the list in half to find a duplicate integer in O(n\lg{n}) time and O(1) space
 * (sort of a modified binary search).
 *
 * But we can actually do better. We can find a duplicate integer in O(n) time while keeping our space cost at O(1).
 *
 * This is a tricky one to derive (unless you have a strong background in graph theory), so we'll get you started:
 *
 * Imagine each item in the list as a node in a linked list. In any linked list, ↴ each node has a value and a "next" pointer. In this case:
 *
 * The value is the integer from the list.
 * The "next" pointer points to the value-eth node in the list (numbered starting from 1).
 * For example, if our value was 3, the "next" node would be the third node.
 *
 * Solution
 * We treat the input list as a linked list like we described at the top in the problem.
 *
 * To find a duplicate integer:
 *
 * We know the position of a node with multiple incoming pointers is a duplicate in our list because the nodes that pointed to it must have the same value.
 *
 * We find a node with multiple incoming pointers by finding the first node in a cycle.
 *
 * We find the first node in a cycle by finding the length of the cycle and advancing two pointers:
 * one starting at the head of the linked list, and the other starting ahead as many steps as there are nodes in the cycle.
 * The pointers will meet at the first node in the cycle.
 *
 * We find the length of a cycle by remembering a position inside the cycle and counting the number of steps it takes to get back to that position.
 *
 * We get inside a cycle by starting at the head and walking nn steps. We know the head of the list is at position n + 1n+1.
 * We want to think of our list as a linked list but we don't want to actually use up all that space,
 * 
 * so we traverse our list as if it were a linked list ↴ by converting positions to indices.
 *
 */
public class FindDuplicateNumberInNPLusOneRangeSpecial {

    public static int findDuplicate(int[] arr) {

        final int n = arr.length - 1;

        // STEP 1: GET INSIDE A CYCLE
        // start at position n+1 and walk n steps to
        // find a position guaranteed to be in a cycle
        int positionInCycle = n + 1;
        for (int i = 0; i < n; i++) {

            // we subtract 1 from the current position to step ahead:
            // the 2nd *position* in an array is *index* 1
            positionInCycle = arr[positionInCycle - 1];
        }

        // STEP 2: FIND THE LENGTH OF THE CYCLE
        // find the length of the cycle by remembering a position in the cycle
        // and counting the steps it takes to get back to that position
        int rememberedPositionInCycle = positionInCycle;
        int currentPositionInCycle = arr[positionInCycle - 1];  // 1 step ahead
        int cycleStepCount = 1;

        while (currentPositionInCycle != rememberedPositionInCycle) {
            currentPositionInCycle = arr[currentPositionInCycle - 1];
            cycleStepCount += 1;
        }

        // STEP 3: FIND THE FIRST NODE OF THE CYCLE
        // start two pointers
        //   (1) at position n+1
        //   (2) ahead of position n+1 as many steps as the cycle's length
        int pointerStart = n + 1;
        int pointerAhead = n + 1;

        //Move the pointer ahead as many cycle steps count to create the stick length, used to cover the cycle
        for (int i = 0; i < cycleStepCount; i++) {
            pointerAhead = arr[pointerAhead - 1];
        }

        // Now, proceed to move both pointer simultaneously (using the stick approach).
        // Advance until the pointers are in the same position (stick covered the cycle), which is the first node in the cycle
        while (pointerStart != pointerAhead) {
            pointerStart = arr[pointerStart - 1];
            pointerAhead = arr[pointerAhead - 1];
        }

        // since there are multiple values pointing to the first node
        // in the cycle, its position is a duplicate in our array
        return pointerStart;
    }

    public static void main(String[] args) {
        int[] arr= {6,7,7,8,9,10,1,2,3,4,5};
        int[] arr1= {6,5,1,3,2,2,2};
        int[] arr2= {6,4,1,1,2,2,1};
        System.out.println(" The duplicated number in arr: "+ Arrays.toString(arr) +" is = " + findDuplicate(arr) );
        System.out.println(" The duplicated number in arr: "+ Arrays.toString(arr1) +" is = " + findDuplicate(arr1) );
        System.out.println(" The duplicated number in arr: "+ Arrays.toString(arr2) +" is = " + findDuplicate(arr2) );
    }
}
