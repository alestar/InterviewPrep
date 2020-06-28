package Problems.BitManipulation;

import java.util.Arrays;

public class IntegerLonely {


    private static int lonelyInteger(int[] arr){
        int result =0;
        for (int value: arr ) {
            result ^= value;
        }
        return result;
    }

    public static void main(String[] args) {
        int[] arr1 = {9,1,2,3,2,9,1,7,7};
        int[] arr2 = {1,2,3,4,5,6,6,5,4,3,2,1,7};

        System.out.println("The Lonley integer for array : '" + Arrays.toString(arr1) + "' is = '" + lonelyInteger(arr1) + "'"); // -> '3'
        System.out.println("The Lonley integer for array : '" + Arrays.toString(arr2) + "' is = '" + lonelyInteger(arr2) + "'"); // -> '7'
    }
}
