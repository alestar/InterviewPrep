package Java.Algorithms.Sorting;

import java.util.Arrays;

// Work on O(nlogn) always but use a los of space everytime O(N)
public class MergeSort {
    private static void mergesort(int[] arr) {
        mergesort(arr,new int[arr.length], 0, arr.length -1);

    }

    private static void mergesort(int[] arr, int[] temp, int leftStart, int rightEnd){
        if(leftStart >= rightEnd){
            return;
        }

        int middle =  (leftStart + rightEnd)/2;
        mergesort(arr, temp, leftStart, middle);
        mergesort(arr,temp, middle +1, rightEnd);
        mergeHalve(arr, temp, leftStart, rightEnd);
    }

    private static void mergeHalve(int[] arr, int[] temp, int leftStart, int rightEnd) {

        int leftEnd = (rightEnd + leftStart) /2;
        int rightStart= leftEnd + 1;
        int size =  rightEnd- leftStart + 1;

        int left = leftStart;
        int right = rightStart;
        int index = leftStart;

        while(left <= leftEnd && right <= rightEnd){
            if(arr[left] < arr[right]){
                temp [index] = arr[left];
                left++;
            }else {
                temp[index] = arr[right];
                right++;
            }
            index++;
        }

        System.arraycopy(arr, left, temp, index,leftEnd - left + 1);
        System.arraycopy(arr, right, temp, index, rightEnd - right + 1);
        System.arraycopy(temp, leftStart, arr, leftStart, size);


    }


    public static void main(String[] args) {
        int[] arr = {6,3,2,1,9,5,7,8,15};
        System.out.println("Array before mergesort: " + Arrays.toString(arr) );

        mergesort(arr);
        System.out.println("Array after mergesort: " + Arrays.toString(arr) );

        int[] arr1 = {10,5,2,7,4,9,12,1,8,6,11,3};
        System.out.println("Array before mergesort: " + Arrays.toString(arr1) );

        mergesort(arr1);
        System.out.println("Array after mergesort: " + Arrays.toString(arr1) );
    }


}
