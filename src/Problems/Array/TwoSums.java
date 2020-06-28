package Problems.Array;


import java.util.Arrays;
import java.util.HashMap;

/**
 * Given an array of int numb find the 2 indices of the numbers that add to a target
 */
public class TwoSums {

    public static int[] findTwoSums(int arr[], int target){
        HashMap<Integer,Integer> values = new HashMap<>();
        int diff= 0;
        for (int i = 0; i < arr.length ; i++) {
            diff = target - arr[i];
            if(!values.containsKey(diff)) {
                values.put(arr[i], i);
                continue;
            }
            else{
                return new int[]{values.get(diff), i};
            }
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        int[] arr= new int[]{2, 7, 11, 15};
        System.out.println("The Two Sums elements index is : " + Arrays.toString(findTwoSums(arr,18)));

    }
}
