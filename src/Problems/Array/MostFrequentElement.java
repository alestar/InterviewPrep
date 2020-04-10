package Problems.Array;
import java.util.Arrays;
import java.util.HashMap;

public class MostFrequentElement {


    // Implement your solution below.
    public static Integer mostFrequent(int[] givenArray) {
        Integer maxCount = -1; Integer maxItem = null;
        HashMap<Integer, Integer> count = new HashMap<Integer, Integer>();
        for (int i : givenArray) {
            if (count.containsKey(i)) {
                Integer newVal = count.get(i) + 1;
                count.put(i, newVal);
            } else {
                count.put(i, 1);
            }
            if (count.get(i) > maxCount) {
                maxCount = count.get(i);
                maxItem = i;
            }
        }
        return maxItem;
    }

    public static void main(String[] args) {
        // NOTE: The following input values are used for testing your solution.


        int[] array1 = {1, 3, 1, 3, 2, 1}; // mostFrequent(array1) should return 1.
        System.out.println("For arr input = " + Arrays.toString(array1));
        System.out.println("The MFE = " + mostFrequent(array1));

        int[] array2 = {3, 3, 1, 3, 2, 1}; // mostFrequent(array2) should return 3.
        System.out.println("For arr input = " + Arrays.toString(array2));
        System.out.println("The MFE = " + mostFrequent(array2));

        int[] array3 = {};// mostFrequent(array3) should return null.
        System.out.println("For arr input = " + Arrays.toString(array3));
        System.out.println("The MFE = " + mostFrequent(array3));

        int[] array4 = {0};// mostFrequent(array4) should return 0.
        System.out.println("For arr input = " + Arrays.toString(array4));
        System.out.println("The MFE = " + mostFrequent(array4));

        int[] array5 = {0, -1, 10, 10, -1, 10, -1, -1, -1, 1}; // mostFrequent(array5) should return -1.
        System.out.println("For arr input = " + Arrays.toString(array5));
        System.out.println("The MFE = " + mostFrequent(array5));
    }
}
