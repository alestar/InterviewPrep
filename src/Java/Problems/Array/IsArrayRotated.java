package Java.Problems.Array;
import java.util.Arrays;

public class IsArrayRotated {

    // Implement your solution below.
    public static Boolean isRotation(int[] array1, int[] array2) {
        if (array1.length != array2.length) return false;
        int key = array1[0];
        int rotPoint = -1;
        for (int i = 0; i < array2.length; i++) {
            if (array2[i] == key) {
                rotPoint = i;
                break;
            }
        }
        if (rotPoint == -1) return false;// I t means no rotation point was found
        for (int i = 0; i < array1.length; i++) {
            int j = (rotPoint + i) % array1.length;// Extrapolate j index to match i
            if (array1[i] != array2[j]) return false;
        }
        return true;//If we reach this point without returning 'false' then it moes be true
    }

    public static void main(String[] args) {
        // NOTE: The following input values will be used for testing your solution.
        int[] array1 = {1, 2, 3, 4, 5, 6, 7};
        int[] array2a = {4, 5, 6, 7, 8, 1, 2, 3};
        // isRotation(array1, array2a) should return false.

        System.out.println("For input : " + Arrays.toString(array1));
        System.out.println("and input : " + Arrays.toString(array2a));
        System.out.println("The output : " +  isRotation(array1, array2a));

        int[] array2b = {4, 5, 6, 7, 1, 2, 3};
        // isRotation(array1, array2b) should return true.
        System.out.println("For input : " + Arrays.toString(array1));
        System.out.println("and input : " + Arrays.toString(array2b));
        System.out.println("The output : " +  isRotation(array1, array2b));


        int[] array2c = {4, 5, 6, 9, 1, 2, 3};
        // isRotation(array1, array2c) should return false.
        System.out.println("For input : " + Arrays.toString(array1));
        System.out.println("and input : " + Arrays.toString(array2c));
        System.out.println("The output : " +  isRotation(array1, array2c));

        int[] array2d = {4, 6, 5, 7, 1, 2, 3};
        // isRotation(array1, array2d) should return false.
        System.out.println("For input : " + Arrays.toString(array1));
        System.out.println("and input : " + Arrays.toString(array2d));
        System.out.println("The output : " +  isRotation(array1, array2d));

        int[] array2e = {4, 5, 6, 7, 0, 2, 3};
        // isRotation(array1, array2e) should return false.
        System.out.println("For input : " + Arrays.toString(array1));
        System.out.println("and input : " + Arrays.toString(array2e));
        System.out.println("The output : " +  isRotation(array1, array2e));

        int[] array2f = {1, 2, 3, 4, 5, 6, 7};
        // isRotation(array1, array2f) should return true.
        System.out.println("For input : " + Arrays.toString(array1));
        System.out.println("and input : " + Arrays.toString(array2f));
        System.out.println("The output : " +  isRotation(array1, array2f));
    }
}
