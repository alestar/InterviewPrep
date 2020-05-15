package Algorithms.Sorting;

import java.util.Arrays;

/**
 * Quick sort is a sorting algorithms that use a pivot to swap elements until the array is in order.
 * Usually works on O(nlogn) depending on how the pivot is selected and space  = O(1) because is based on swapping element rather than creating a copy of the array
 *
 */
public class QuickSort {

    public static void quicksort(int[] array){
        quicksort(array,0,array.length -1);
    }

    private static void quicksort(int[] array, int left, int right) {
        if(left >= right)
            return;;

        int pivot = array[(left + right) / 2];
        int index = partition(array, left, right, pivot);
        quicksort(array, left, index-1);
        quicksort(array, index, right);
    }

    private static int partition(int[] array, int left, int right, int pivot) {
        while (left <= right){
            while(array[left] < pivot) {
                left++;
            }
            while(array[right] > pivot) {
                right--;
            }
            if(left <= right) {
                swap(array, left, right);
                left++;
                right--;
            }
        }
        return left;

    }

    private static void swap(int [] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    public static void main(String[] args) {
        int[] arr = {6,3,2,1,9,5,7,8,15};
        System.out.println("Array before quicksort: " + Arrays.toString(arr) );

        quicksort(arr);
        System.out.println("Array after quicksort: " + Arrays.toString(arr) );

        int[] arr1 = {10,5,2,7,4,9,12,1,8,6,11,3};
        System.out.println("Array before quicksort: " + Arrays.toString(arr1) );

        quicksort(arr1);
        System.out.println("Array after quicksort: " + Arrays.toString(arr1) );

    }
}
