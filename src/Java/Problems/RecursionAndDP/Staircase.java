package Java.Problems.RecursionAndDP;

// Recursive solution using dynamic programming

//  Time Complexity: O(n)
// Space Complexity: O(n)

// Can alternatively be solved in O(1) space (per testcase) by using iteration instead of recursion

import java.util.HashMap;
import java.util.Scanner;

public class Staircase {
    private static HashMap<Integer, Integer> cache = new HashMap();

    //Time = O(n) , Space = O(n) - Linear
    //NOte without memo the recursive approach is exponential!!!
    private static int countPathRcsv(int steps) {
        if(steps <0){
            return 0;
        }
        return countPathMemo(steps, new int[steps + 1]);
    }

    private static int countPathMemo(int steps, int[] memo) {
        if (steps < 0) {
            return 0;
        }
        else if(steps == 0){
            return 1;
        }
        if(memo[steps] == 0) {

            memo[steps] = staircase(steps - 1) + staircase(steps - 2) + staircase(steps - 3);
        }
        return memo[steps];
    }


    //Time = O(n) , Space = O(n) - Linear
    private static int countPathIter(int steps, int[] memo) {
        if (steps < 0) {
            return 0;
        }
        else if(steps == 0){
            return 1;
        }
        int[] paths = new int[steps + 1];
        paths[0] = 1;
        paths[1] = 1;
        paths[2] = 2;
        for (int i = 3; i < steps; i++) {

            paths[i] = paths[i - 1] + paths[i - 2] + paths[i - 3];
        }
        return paths[steps];
    }

    //Time = O(n) , Space = O(1) - Linear and Optimal
    private static int countPathIterOpt(int steps, int[] memo) {
        if (steps < 0) {
            return 0;
        }
        else if(steps == 0){
            return 1;
        }
        int[] paths = {1,1,2};
        for (int i = 3; i < steps; i++) {

            int count = paths[2] + paths[1] + paths[0];
            paths[0] = paths[1];
            paths[1] = paths[2];
            paths[2] = count;
        }
        return paths[steps];
    }

    //Time = O(n) , Space = O(n)
    private static int staircase(int n) {
        if (n < 0) {
            return 0;
        }
        if (cache.containsKey(n)) {
            return cache.get(n);
        }
        int ways = staircase(n - 1) + staircase(n - 2) + staircase(n - 3);
        cache.put(n, ways);
        return ways;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int testcases = scan.nextInt();
        cache.put(0, 1); // base case
        while (testcases-- > 0) {
            int n = scan.nextInt();
            System.out.println(staircase(n));
        }
        scan.close();
    }
}
