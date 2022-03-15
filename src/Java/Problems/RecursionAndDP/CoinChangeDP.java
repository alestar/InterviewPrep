package Java.Problems.RecursionAndDP;

/**
 *
 * Problem Statement-
 * [DP: Coin Change](https://www.hackerrank.com/challenges/ctci-coin-change/problem)
 *
 */

import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

/**
 * @author Kanahaiya Gupta
 *
 */
public class CoinChangeDP {
    /**
     * @Approach1: Recursion
     *
     * @param n
     * @param coins
     */
    private static void approach1(int n, int[] coins) {
        long result = noOfWaysToGetChangeUsingRecusion(coins, n, 0);
        System.out.println(result);
    }

    /**
     * @Approach1: Recursion
     *
     * @param coins
     * @param money
     * @return
     */
    private static long noOfWaysToGetChangeUsingRecusion(int[] coins, int money, int index) {
        if (money == 0)
            return 1;
        if (money < 0 || index >= coins.length)
            return 0;
        return noOfWaysToGetChangeUsingRecusion(coins, money - coins[index], index)
                + noOfWaysToGetChangeUsingRecusion(coins, money, index + 1);
    }

    /**
     *@Approach2: Recursion with Memoization
     *
     * @param money
     * @param coins
     */
    private static void approach2(int money, int[] coins) {
        long memo[][] = new long[money + 1][coins.length + 1];
        memo[0][0] = 1;
        long result = noOfWaysToGetChangeUsingRecursionWithMemo(coins, money, 0, memo);
        System.out.println(result);
    }

    /**
     * @Approach2: Recursion with Memoization
     *
     * @param coins
     * @param money
     * @return
     */
    private static long noOfWaysToGetChangeUsingRecursionWithMemo(int[] coins, int money, int index, long[][] memo) {
        if (money == 0)
            return 1;
        if (money < 0 || index >= coins.length)
            return 0;
        if (memo[money][index] != 0)
            return memo[money][index];
        return memo[money][index] = noOfWaysToGetChangeUsingRecursionWithMemo(coins, money - coins[index], index, memo)
                + noOfWaysToGetChangeUsingRecursionWithMemo(coins, money, index + 1, memo);
    }

    /**
     * @Approach3 : Recursion with Memoization with Hashmap(alternate of method2)
     *
     * @param money
     * @param coins
     */
    private static void approach3(int money, int[] coins) {
        long result = noOfWaysToGetChangeUsingDP(coins, money);
        System.out.println(result);
    }

    /**
     * @Approach3 : Recursion with Memoization with Hashmap(alternate of method2)
     *
     * @param coins
     * @param money
     * @return
     */
    private static long noOfWaysToGetChangeUsingRecursionWithMemo2(int[] coins, int money) {
        return makeChange(coins, money, 0, new HashMap<String, Long>());
    }

    private static long makeChange(int[] coins, int money, int index, HashMap<String, Long> memo) {
        if (money == 0)
            return 1;
        if (index >= coins.length)
            return 0;

        String key = money + "-" + index;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }

        int amountWithCoin = 0;
        long ways = 0;
        while (amountWithCoin <= money) {
            int remaining = money - amountWithCoin;
            ways += makeChange(coins, remaining, index + 1, memo);
            amountWithCoin += coins[index];
        }
        memo.put(key, ways);
        return ways;
    }

    /**
     * @Approach4: Using dynamic programming approach
     *
     * @param money
     * @param coins
     */
    private static void approach4(int money, int[] coins) {
        long result = noOfWaysToGetChangeUsingRecursionWithMemo2(coins, money);
        System.out.println(result);
    }

    /**
     * @Approach4: Using dynamic programming approach
     *
     * @param coins
     * @param money
     * @return
     */
    private static long noOfWaysToGetChangeUsingDP(int[] coins, int money) {
        long dp[] = new long[money + 1];
        dp[0] = 1;
        for (int coin : coins) {
            for (int j = coin; j <= money; j++) {
                dp[j] += dp[j - coin];
            }
        }
        return dp[money];
    }

/*    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        int coins[] = new int[m];
        for (int coins_i = 0; coins_i < m; coins_i++) {
            coins[coins_i] = in.nextInt();
        }
//	        approach1(n, coins);
//	        approach2(n, coins);
        approach3(n, coins);
//	        approach4(n, coins);
        in.close();
    }*/

    public static void main(String[] args) {
        int[] coins1 = {50,25,10,5,1};
        int[] coins2 = {25,10,5,1};
        int[] coins3 = {10,5,1};
        int money1 = 79;
        System.out.println("Coins1 to use as change : " + Arrays.toString(coins1) );
        System.out.println("    for money1 : " + money1 );
        System.out.println("    ways to give change: " + noOfWaysToGetChangeUsingDP(coins1,money1) );

        System.out.println("Coins2 to use as change : " + Arrays.toString(coins2) );
        System.out.println("    for money1 : " + money1 );
        System.out.println("    ways to give change: " + noOfWaysToGetChangeUsingDP(coins2,money1) );

        System.out.println("Coins3 to use as change : " + Arrays.toString(coins3) );
        System.out.println("    for money1 : " + money1 );
        System.out.println("    ways to give change: " + noOfWaysToGetChangeUsingDP(coins3,money1) );
    }

}
