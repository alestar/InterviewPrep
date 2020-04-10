package Problems.Array.Subset;

import java.util.Arrays;
import java.util.HashMap;

/**
 * Created by Alestar on 3/17/2019.
 */
public class SubSetSum {

    public static int countSubSetRecv(int[] arr, int total) {
        return findSubSetSumRecv(  arr,  total, arr.length -1);
    }

    public static int countSubMemo(int[] arr, int total) {
        HashMap<String, Integer> memo= new HashMap<>();
        return findSubSetSumMemo(  arr,  total, arr.length -1, memo);
    }

    public static int findSubSetSumRecv(int[] arr, int total, int index) {

        if (total == 0) // The empty set that add up to '0' is still consider a set, therefore '1' is returned
            return 1;
        else if (total < 0) // If only positive numbers are used is imposible to return a Set that addup to negative, therefore '0' is returned
            return 0;
        else if (index < 0) // arr out of bound
            return 0;
        else if (arr[index] > total) {// if the current number is bigger than the 'total', then this current number can not be included in subset that add up to 'total';
            // it will be bigger, it most be excluded
            return findSubSetSumRecv(arr, total, index - 1);// move to the next element in the array
        } else {// (2) scenarios to find subsets:
            //(1) -  Include current number. Add Subsets than can conform 'total' using current number,
            // which is equivalent to find subsets that can conform the complement, the (total - current) number.
            //(2) -  Don't include current number.Add Subsets than can conform 'total' without using current number.
            return findSubSetSumRecv(arr, total - arr[index], index - 1) + findSubSetSumRecv(arr, total, index - 1);
        }

}

    public static int findSubSetSumMemo(int [] arr, int total, int index, HashMap<String, Integer> memo){
        String key= Integer.toString(total) + ':' + Integer.toString(index);
        System.out.println("Created 'key' = " + key );

        int result=0;
        if(memo.containsKey(key)){//Create compound key
            System.out.println("Total 'memo' [" + memo.keySet().size() + "]");
            return memo.get(key);
        }
        if(total == 0) // The empty set that add up to '0' is still consider a set, therefore '1' is returned
            return 1;
        else if(total < 0) // If only positive numbers are used is imposible to return a Set that addup to negative, therefore '0' is returned
            return 0;
        else if(index < 0) // arr out of bound
            return 0;
        else if (arr[index] > total) {// if the current number is bigger than the 'total', then this current number CAN NOT be included in subset that conforms or adds up to 'total';
                                        // because the sum of elements would be bigger than 'total', therefore it most be excluded as a possible member of a subset and keep looking.
            result= findSubSetSumMemo(arr, total, index - 1,memo);// move to the next element in the array
        }
        else{// (2) scenarios to find subsets:
                //(1) -  Include current number. Add Subsets than can conform 'total' using 'current' number,
                // which is equivalent to find subsets that can conform the complement(the <total - current> number).
                // If a subsets can conform the complement, then adding 'current' number would have create subset that can conform the 'total'.
                //(2) -  Don't include current number. Add Subsets than can conform 'total' without using current number.
            result=  findSubSetSumMemo(arr,total - arr[index],index-1,memo) + findSubSetSumRecv(arr,total,index-1);
        }
        memo.put(key,result);
        return result;
    }

    public static void main(String args[]){

        int arr[] = {2,4,6,10};
        int sum= 16;
        //int arr[] = {20,10,1,9,4,6};
        //int sum= 20;

        System.out.println("Input arr = " + Arrays.toString(arr) );
        System.out.println("Input 'sum' = " + sum);

        int res= countSubMemo(arr,sum);
        System.out.println("Total Number of Subsets found that add to 'sum'= " + res);
    }
}
