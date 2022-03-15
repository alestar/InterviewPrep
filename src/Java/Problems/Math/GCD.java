package Java.Problems.Math;

/**
 * Created by Alestar on 1/8/2019.
 */

// Java program to find Java.Problems.Math.GCD of two or
// more numbers

public class GCD {
    // Function to return gcd of a and b
    static int gcd(int a, int b)
    {
       System.out.println("Calculating Java.Problems.Math.GCD: ");
       System.out.println("    with current 'a' = " + a);
       System.out.println("    with current 'b' = " + b);
       if (a == 0)
           return b;
       System.out.println("    where 'b%a' = " + b%a);
       return gcd(b % a, a);
    }

    // Function to find gcd of array of
    // numbers
    static int findGCD(int arr[], int n)
    {
        int result = arr[0];
        for (int i = 1; i < n; i++)
            result = gcd(arr[i], result);

        return result;
    }

    public static void main(String[] args)
    {
        int arr[] = {4 , 2};
        int n = arr.length;
        System.out.println("The Java.Problems.Math.GCD value is: " + findGCD(arr, n));
    }
}
