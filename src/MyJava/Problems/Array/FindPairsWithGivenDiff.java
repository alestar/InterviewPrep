package MyJava.Problems.Array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * Created by Alestar on 1/12/2019.
 */
public class FindPairsWithGivenDiff {


    static int[][] findPairsWithGivenDifference(int[] arr, int k) {
        //Validate paramaters and return empty
        if((arr.length == 0) || (k == 0)){
            return new int[0][];
        }
        //Loop for adding all items to the Set to later compair if the complement exist already
        Set<Integer> comp = new HashSet<>();
        for(int i=0; i< arr.length; i++){
            if(!comp.contains(arr[i])){
                comp.add(arr[i]);
            }
        }
        //Loop to verify if the complement exist in the Set to then create the pairs
        ArrayList<int[]> list=new ArrayList<int[]>();
        for(int i=0; i< arr.length; i++){
            int c= k + arr[i];
            if(comp.contains(c)){
                int pair[]={c,arr[i]};
                list.add(pair);
            }
        }

        //Create result array[][] from the list
        int[][] result= new int[list.size()][];
        int index=0;
        for (int[] item : list) {
            result[index] = item;
            index++;
        }
        return result;
    }

    public static void main(String[] args) {
        int [] arr = {1,2,4,5,8,9,10};
        System.out.println("Results 'k=5': " + Arrays.deepToString(findPairsWithGivenDifference(arr,5)));
        System.out.println("Results 'k=2': " + Arrays.deepToString(findPairsWithGivenDifference(arr,2)));
        System.out.println("Results 'k=1': " + Arrays.deepToString(findPairsWithGivenDifference(arr,1)));
        System.out.println("Results 'k=3': " + Arrays.deepToString(findPairsWithGivenDifference(arr,3)));
        System.out.println("Results 'k=0': " + Arrays.deepToString(findPairsWithGivenDifference(arr,0)));
    }
}
