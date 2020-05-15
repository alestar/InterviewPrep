package Problems.RecursionAndDP;

import java.util.Arrays;
import java.util.HashMap;

public class CoinChange {

    public static long makeChangeRecsv(int[] coins, int money) {

        return makeChangeRecsv(coins,money,0, new HashMap<>());
    }

    public static long makeChangeRecsv(int[] coins, int money, int index, HashMap<String,Long> memo) {
        if (money == 0){
            return 1;
        }

        if(index >= coins.length){
            return  0;
        }

        String key =  money + "-" + index; // Use the separator '-' to distinct comb "29" + "1" || "2" + "91"
        if(memo.containsKey(key)){
            return memo.get(key);
        }

        int amountWithCoin= 0;
        long ways =0;
        while(amountWithCoin <= money){

            int remaining = money - amountWithCoin;
            ways += makeChangeRecsv(coins, remaining, index +1, memo);
            amountWithCoin += coins[index];

        }
        memo.put(key,ways);
        return ways;
    }

    private static long makeChangeIter(int[] coins, int money) {
        long ways[] = new long[money + 1];
        ways[0] = 1;
        for (int coin : coins) {
            for (int current = coin; current <= money; current++) {
                int prev = current - coin;
                ways[current] += ways[prev];
            }
        }
        return ways[money];
    }



    public static void main(String[] args) {
        int[] coins1 = {50,25,10,5,1};
        int[] coins2 = {25,10,5,1};
        int[] coins3 = {10,5,1};
        int money1 = 79;
        System.out.println("Coins1 to use as change : " + Arrays.toString(coins1) );
        System.out.println("    for money1 : " + money1 );
        System.out.println("    ways to give change: " + makeChangeRecsv(coins1,money1) );

        System.out.println("Coins2 to use as change : " + Arrays.toString(coins2) );
        System.out.println("    for money1 : " + money1 );
        System.out.println("    ways to give change: " + makeChangeRecsv(coins2,money1) );

        System.out.println("Coins3 to use as change : " + Arrays.toString(coins3) );
        System.out.println("    for money1 : " + money1 );
        System.out.println("    ways to give change: " + makeChangeRecsv(coins3,money1) );
    }

}
