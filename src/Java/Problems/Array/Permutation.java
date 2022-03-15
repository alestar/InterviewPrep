package Java.Problems.Array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Stream;

public class Permutation {


    public static <T> T[][] permuteRecvSwap(T[] arr){
        return convertListToMultiArr(permuteRecvSwap(arr,0),arr.length);
    }

    /**
    NOTE: Not optimal a copy of the arr needs to be created every time the array is swapped to keep a swapped copy.
     */
    public static <T> List<T[]> permuteRecvSwap(T[] arr, int current) {

        List<T[]> list = new ArrayList<T[]>();

        if(current == arr.length -1) {
            list.add(arr);
            return list;
        }

        for (int i = current; i < arr.length; i++) {
            swap(arr,current,i);
            T[] arr_swaped = Arrays.copyOf(arr,arr.length);
            list.addAll(permuteRecvSwap(arr_swaped,current + 1));
        }
        return list;
    }


    public static <T> T[][] permuteExclude(T[] arr) {
        return convertListToMultiArr(permuteExclude(arr, new ArrayList<T>()), arr.length);
    }

    public static <T> List<T[]> permuteExclude(T[] arr, List<T> val) {

        if(arr.length == 1 ) {
            val.add(arr[0]);
            return Collections.singletonList(((T[]) val.toArray()));
        }
        List<T[]> result = new ArrayList<T[]>();
        for (int i = 0; i < arr.length; i++) {
            T[] subarr = null;
            if(arr.length == 2 ){
                if( i == 1 )
                    subarr = Arrays.copyOfRange(arr, 0, i);
                else
                    subarr = Arrays.copyOfRange(arr, i + 1, arr.length);
            }
            else if(arr.length > 2 ) {
                T[] arrLeft = Arrays.copyOfRange(arr, 0, i);
                T[] arrRight = Arrays.copyOfRange(arr, i == arr.length - 1 ? i : i + 1, arr.length);
                subarr = (T[]) Stream.of(arrLeft, arrRight).flatMap(Stream::of).toArray();
            }
            val.add(arr[i]);
            result.addAll( permuteExclude(subarr,val));
            val = new ArrayList<T>();
        }

        return result;
    }


    //Aux
    public static final <T> void swap (T[] a, int i, int j) {
        T n = a[i];
        a[i] = a[j];
        a[j] = n;
    }

    private static <T> T[][] convertListToMultiArr(List<T[]> list, int n){

        T[][] result=  (T[][]) new Object[list.size()][n];
        int index=0;
        for (T[] item : list) {
            result[index] = item;
            index++;
        }
        return result;
    }

    public static void main(String[] args) {
        Integer[] arr1 = {1,2,3};
        System.out.println("Permutations for 'arr': " +Arrays.toString(arr1) + " contains: " + Arrays.deepToString(permuteRecvSwap(arr1)));
        Integer[] arr2 = {1,2,3};
        System.out.println("Permutations for 'arr': " +Arrays.toString(arr2) + " contains: " + Arrays.deepToString(permuteExclude(arr2)));

    }
}
