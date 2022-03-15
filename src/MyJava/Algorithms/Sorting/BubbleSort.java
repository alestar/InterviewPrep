package MyJava.Algorithms.Sorting;

import java.util.Arrays;

/**
 *  Bublle sor is O(n^2) but does not required space
 */
public class BubbleSort {

    private static void bubbleSort(int[] a) {

        boolean isSorted = false;
        int lastUnsorted = a.length -1;

        while (!isSorted){
            isSorted=true;
            for (int i = 0; i < lastUnsorted; i++) {
                if(a[i] > a[i+1] ){
                    swap(a,i,i +1);
                    isSorted = false;
                }
            }
            lastUnsorted--;
        }
    }

    private static void swap( int[] a, int i, int j) {
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }

    public static void main(String[] args) {
        int[] arr = {6,3,2,1,9,5,7,8,15};
        System.out.println("Array before bubbleSort: " + Arrays.toString(arr) );

        bubbleSort(arr);
        System.out.println("Array after bubbleSort: " + Arrays.toString(arr) );

        int[] arr1 = {10,5,2,7,4,9,12,1,8,6,11,3};
        System.out.println("Array before bubbleSort: " + Arrays.toString(arr1) );

        bubbleSort(arr1);
        System.out.println("Array after bubbleSort: " + Arrays.toString(arr1) );
    }


}
