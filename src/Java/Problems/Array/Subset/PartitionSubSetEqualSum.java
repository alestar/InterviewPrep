package Java.Problems.Array.Subset;

/**
 * Created by Alestar on 4/27/2019.
 */

import java.util.Arrays;

/**
 Given a non-empty array containing only positive integers,
 find if the array can be partitioned into two subsets
 such that the sum of elements in both subsets is equal.

 Note:
 Each of the array element will not exceed 100.
 The array size will not exceed 200.

 Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is same.

 Example:
     arr[] = {1, 5, 11, 5}
     Output: true
     The array can be partitioned as {1, 5, 5} and {11}

     arr[] = {1, 5, 3}
     Output: false
     The array cannot be partitioned into equal sum sets.

 Following are the two main steps to solve this problem:
     1) Calculate sum of the array. If sum is odd, there can not be two subsets with equal sum, so return false.
     2) If sum of array elements is even, calculate sum/2 and find a subset of array with sum equal to sum/2.

 The first step is simple. The second step is crucial, it can be solved either using recursion or Dynamic Programming.

 Following is the recursive property of the second step mentioned above.

 Let isSubsetSum(arr, n, sum/2) be the function that returns true if
 there is a subset of arr[0..n-1] with sum equal to sum/2

 The isSubsetSum problem can be divided into two sub-problems
     a) isSubsetSum() without considering getLast element(reducing n to n-1)
     b) isSubsetSum considering the getLast element(reducing sum/2 by arr[n-1] and n to n-1)

 If any of the above the above sub-problems return true, then return true.
 isSubsetSum (arr, n, sum/2) = isSubsetSum (arr, n-1, sum/2) || isSubsetSum (arr, n-1, sum/2 - arr[n-1])

 * */

public class PartitionSubSetEqualSum {

    // A recursive Java solution for partition problem
    // Returns true if arr[] can be partitioned in two
    // subsets of equal sum, otherwise false
    static boolean findPartition (int arr[], int n)
    {
        if(n ==0)//Empty array
            return false;

        // Calculate sum of the elements in array
        int sum = 0;
        for (int i = 0; i < n; i++)
            sum += arr[i];

        // If sum is odd, there cannot be two subsets
        // with equal sum
        if (sum%2 != 0)
            return false;

        // Find if there is subset with sum equal to half
        // of total sum
        return isSubsetSum (arr, n, sum/2);
    }


    // A utility function that returns true if there is a
    // subset of arr[] with sun equal to given sum
    static boolean isSubsetSum (int arr[], int n, int sum)
    {
        // Base Cases
        if (sum == 0)
            return true;
        if (n == 0 && sum != 0)
            return false;

        // If getLast element is greater than sum, then ignore it
        if (arr[n-1] > sum)
            return isSubsetSum (arr, n-1, sum);

    /* else, check if sum can be obtained by any of
       the following
    (a) including the getLast element
    (b) excluding the getLast element
    */
        return isSubsetSum (arr, n-1, sum) || isSubsetSum (arr, n-1, sum - arr[n-1]);
    }


    /*Driver function to check for above function*/
    public static void main (String[] args)
    {
        //True cases
        int arr[] = {3, 1, 5, 9, 12};// Should return 'true' because the array can be partitioned as : {12,3} and {1,5,9} add up to 15
        System.out.println("Findings partition equal sum for input: " + Arrays.toString(arr));
        System.out.println("Can be divided into two subsets of equal sum? :  " + findPartition(arr, arr.length));

        int arr1[] = {1, 5, 11, 5};// Should return 'true' because the array can be partitioned as {1, 5, 5} and {11}, which add up to 11
        System.out.println("Findings partition equal sum for input: " + Arrays.toString(arr1));
        System.out.println("Can be divided into two subsets of equal sum? : " + findPartition(arr1, arr1.length));

        int arr2[] = {1, 5, 12, 6};// Should return 'true' because the array can be partitioned as {1, 5, 6} and {12}, which add up to 12
        System.out.println("Findings partition equal sum for input: " + Arrays.toString(arr2));
        System.out.println("Can be divided into two subsets of equal sum? : " + findPartition(arr2, arr2.length));

        //False Cases
        int arr3[] = {1, 5, 3};// Should return 'false' because the array cannot be partitioned into equal sum sets.
        System.out.println("Findings partition equal sum for input: " + Arrays.toString(arr3));
        System.out.println("Can be divided into two subsets of equal sum? : " + findPartition(arr3, arr3.length));

        int arr4[] = {};// Should return 'false' because the array cannot be partitioned into equal sum sets.
        System.out.println("Findings partition equal sum for input: " + Arrays.toString(arr4));
        System.out.println("Can be divided into two subsets of equal sum? : " + findPartition(arr4, arr4.length));
    }
}

