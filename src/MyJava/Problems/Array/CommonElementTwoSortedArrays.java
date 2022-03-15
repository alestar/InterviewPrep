package MyJava.Problems.Array;
import java.util.ArrayList;
import java.util.Arrays;

public class CommonElementTwoSortedArrays {
    // Implement your solution below.
    // NOTE: Remember to return an Integer array, not an int array.
    public static Integer[] commonElements(int[] array1, int[] array2) {
        int p1 = 0;
        int p2 = 0;
        // Need to use ArrayList because we don't know the size of the resulting
        // array yet. Note that an ArrayList is resizable.
        ArrayList<Integer> result = new ArrayList();
        while(p1 < array1.length && p2 < array2.length){
            if (array1[p1] == array2[p2]) {
                result.add(array1[p1]);
                p1 += 1;
                p2 += 1;
            }
            else if (array1[p1] > array2[p2]) {
                p2 += 1;
            } else {
                p1 += 1;
            }
        }
        // Convert the result to a regular array.
        Integer[] resultInArray = new Integer[result.size()];
        return result.toArray(resultInArray);
    }
    public static void main(String[] args) {
        // NOTE: The following input values are used for testing your solution.

        int[] array1A = {1, 3, 4, 6, 7, 9};
        int[] array2A = {1, 2, 4, 5, 9, 10};
        // commonElements(array1A, array2A) should return [1, 4, 9] (an array).

        System.out.println("For input = " + Arrays.toString(array1A));
        System.out.println("and input = " + Arrays.toString(array2A));
        System.out.println("The output = " +  Arrays.toString(commonElements(array1A, array2A)));


        int[] array1B = {1, 2, 9, 10, 11, 12};
        int[] array2B = {0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15};
        // commonElements(array1B, array2B) should return [1, 2, 9, 10, 12] (an array).

        System.out.println("For input = " + Arrays.toString(array1B));
        System.out.println("and input = " + Arrays.toString(array2B));
        System.out.println("The output = " +  Arrays.toString(commonElements(array1B, array2B)));

        int[] array1C = {0, 1, 2, 3, 4, 5};
        int[] array2C = {6, 7, 8, 9, 10, 11};
        // common_elements(array1C, array2C) should return [] (an empty array).

        System.out.println("For input = " + Arrays.toString(array1C));
        System.out.println("and input = " + Arrays.toString(array2C));
        System.out.println("The output = " +  Arrays.toString(commonElements(array1C, array2C)));
    }
}
