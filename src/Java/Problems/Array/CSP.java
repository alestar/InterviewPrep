package Java.Problems.Array;

import java.util.Arrays;

public class CSP {

    public static int[] closestSumPair(int[] a1, int[] a2, int target) {
        int[] a1Sorted = Arrays.copyOf(a1, a1.length);
        Arrays.sort(a1Sorted);
        int[] a2Sorted = Arrays.copyOf(a2, a2.length);
        Arrays.sort(a2Sorted);

        int i = 0;
        int j = a2Sorted.length - 1;
        int smallestDiff = Math.abs(a1Sorted[0] + a2Sorted[0] - target);
        int[] closestPair = {a1Sorted[0], a2Sorted[0]};

        while (i < a1Sorted.length && j >= 0 ) {
            int v1 = a1Sorted[i];
            int v2 = a2Sorted[j];
            int currentDiff = v1 + v2 - target;
            if (Math.abs(currentDiff) < smallestDiff) {
                smallestDiff = Math.abs(currentDiff);
                closestPair[0] = v1; closestPair[1] = v2;
            }

            if (currentDiff == 0) {
                return closestPair;
            }
            else if (currentDiff < 0) {
                i += 1;
            }
            else {
                j -= 1;
            }
        }

        return closestPair;
    }

    public static void main(String[] args) {
        // NOTE: You can use the following input values to test this function.

        // a1 and a2 are the given arrays, and target is the target sum.
        // It should return an array of two numbers as the result,
        // one from each array.

        int[] a1 = {-1, 3, 8, 2, 9, 5};
        int[] a2 = {4, 1, 2, 10, 5, 20};
        int aTarget = 24;//  should return {5, 20} or {3, 20}

        System.out.println("For a1[] input: " + Arrays.toString(a1));
        System.out.println("And a2[] input: " + Arrays.toString(a2));
        System.out.println("And aTarget input: " + aTarget);
        System.out.println("The closes Sum Pair is: " + Arrays.toString(closestSumPair(a1, a2, aTarget)));

        int[] b1 = {7, 4, 1, 10};
        int[] b2 = {4, 5, 8, 7};
        int bTarget = 13;//should return {4, 8}, {7, 7}, {7, 5}, or {10, 4}

        System.out.println("For b1[] input: " + Arrays.toString(b1));
        System.out.println("And b2[] input: " + Arrays.toString(b2));
        System.out.println("And bTarget input: " + bTarget);
        System.out.println("The closes Sum Pair is: " + Arrays.toString(closestSumPair(b1, b2, bTarget) ));

        int[] c1 = {6, 8, -1, -8, -3};
        int[] c2 = {4, -6, 2, 9, -3};
        int cTarget = 3; // should return {-1, 4} or {6, -3}

        System.out.println("For c1[] input: " + Arrays.toString(c1));
        System.out.println("And c2[] input: " + Arrays.toString(c2));
        System.out.println("And cTarget input: " + cTarget);
        System.out.println("The closes Sum Pair is: " + Arrays.toString(closestSumPair(c1, c2, cTarget) ));

        int[] d1 = {19, 14, 6, 11, -16, 14, -16, -9, 16, 13};
        int[] d2 = {13, 9, -15, -2, -18, 16, 17, 2, -11, -7};
        int dTarget = -15;//  should return {-16, 2}, {-9, -7}

        System.out.println("For d1[] input: " + Arrays.toString(d1));
        System.out.println("And d2[] input: " + Arrays.toString(d2));
        System.out.println("And dTarget input: " + dTarget);
        System.out.println("The closes Sum Pair is: " + Arrays.toString(closestSumPair(d1, d2, dTarget) ));
    }

}
