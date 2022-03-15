package Java.Problems.Array;

import java.util.Arrays;

/**
 * Created by Alestar on 3/22/2019.

// Question :
// Given an array containing only 0's and 1's,
// write an algorithm / program to find the largest sub-array with equal number of 0's and 1's.

// [0,0,0,0,0,1,1,1,1]
// OUTPUT : StartIndex = 1, EndIndex = 8

// [0,1,0,1,0,1,0,1]
// OUTPUT : StartIndex = 0, EndIndex = 7 , i.e full array

// [0,0,0,0,0,0,1]
// OUTPUT : StartIndex = 5, EndIndex = 6 , i.e getLast 2 elements

// [1,1,1,1,1]
// OUTPUT : No such case exists

// [0,0,0,0,0]
// OUTPUT : No such case exists


// [0,0,0,1,0,0,0,0]
// OUTPUT : StartIndex = 2, EndIndex = 3
// OUTPUT : StartIndex = 3, EndIndex = 4

// [0,0,0,1,1,0,0,1,0,0]
// OUTPUT : StartIndex = 2, EndIndex = 7... 0,1,1,0,0,1

 */

public class LongestBinarySubArray  {

    public static void solBruteForce(int arr[]){

        System.out.println("Using arr = " + Arrays.toString(arr));

        int n = arr.length;
        int countCeros=0;
        int countOne=0;
        int max_subarr=0;
        int current_max_subarr=0;
        int start=-1;
        int end=-1;


        for(int i=0; i<n; i++){
            countCeros=0;
            countOne=0;
            for(int j=i; j < n; j++){

                if(arr[j] == 0)
                    countCeros++;
                else
                    countOne++;

                if(countCeros == countOne){
                    current_max_subarr= (j-i) + 1;
                    if(current_max_subarr > max_subarr){
                        max_subarr = current_max_subarr;
                        start = i;
                        end = j;
                    }
                }
            }
        }
        if(start==-1 || end==-1)
            System.out.println("No sub-arr exists for arr + " + Arrays.toString(arr));
        else{
            System.out.println("Sub-arr size = [" + max_subarr + "]");
            System.out.println("Starting index = '" + start + "'");
            System.out.println("Starting end = '" + end + "'");
        }
    }

    public static void solOptimal(int arr[]) {  // O(n)

        int n = arr.length;
        int start =-1;
        int end=-1;
        int countCeros=0;
        int countOne=0;
        for(int i=0; i<n; i++) {

            if (arr[i] == 0)
                countCeros++;
            else
                countOne++;

            if (i+1 < n && arr[i] != arr[i + 1] && start == -1) {
                start = i;

                if(arr[i] == 0) {// Reset copunter for sub-array
                    countCeros = 1;
                    countOne = 0;
                }
                else{
                    countCeros = 0;
                    countOne = 1;
                }
            }
            if (start != -1 && countCeros == countOne){
                end = i;
            }
        }
        if(start == -1 || end == -1)
            System.out.println("(Sol Opt) No sub-arr exists for arr + " + Arrays.toString(arr));
        else{
            //System.out.println("Sub-arr size = [" + max_subarr + "]");
            System.out.println("(Sol Opt)Starting index = '" + start + "'");
            System.out.println("(Sol Opt) Starting end = '" + end + "'");
        }
    }

    public static void main(String args[] ) throws Exception {

        int arr[] = {0,0,0,1,1,0,0,1,0,0}; // OUTPUT : StartIndex = 2, EndIndex = 7 Sub-arr size = [6]
        solBruteForce(arr);
        solOptimal(arr);

        int arr1[] = {0,0,0,1,0,0,0,0};  // OUTPUT : StartIndex = 2, EndIndex = 3 Sub-arr size = [2]
        solBruteForce(arr1);
        solOptimal(arr1);

        int arr2[] = {0,0,0,0,0,0,1};    // OUTPUT : StartIndex = 5, EndIndex = 6 Sub-arr size = [2] (i.e getLast 2 elements)
        solBruteForce(arr2);
        solOptimal(arr2);

        int arr3[] = {0,1,0,1,0,1,0,1};  // OUTPUT : StartIndex = 0, EndIndex = 7 Sub-arr size = [8] (i.e full array)
        solBruteForce(arr3);
        solOptimal(arr3);

        int arr4[] = {0,0,0,0,1,1,1,1};  // OUTPUT : StartIndex = 0, EndIndex = 7  Sub-arr size = [8] (i.e full array)
        solBruteForce(arr4);
        solOptimal(arr4);

        int arr5[] = {1,1,0,0,1,1,1,1};  // OUTPUT : StartIndex = 0, EndIndex = 3 Sub-arr size = [4],
        solBruteForce(arr5);
        solOptimal(arr5);

        int arr10[] = {1,1,1,1,1}; // No such case exists
        solBruteForce(arr10);
        solOptimal(arr10);

    }

}
