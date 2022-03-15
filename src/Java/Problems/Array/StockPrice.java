package Java.Problems.Array;

import java.util.HashMap;

/**
 * Created by Alestar on 1/12/2019.
 */
public class StockPrice {


    public static int getMaxProfitMap(int[] stockPrices) {

        if(stockPrices.length< 2)
            throw new IllegalArgumentException("Can not calculate profit with just 1 stock price");

        HashMap<Integer,Integer> map = new HashMap<>();
        int mimPrice = stockPrices[0];
        int maxPrice = stockPrices[1];
        int maxProfit = maxPrice - mimPrice;
        map.put(mimPrice,0);
        for (int i = 1; i < stockPrices.length ; i++) {
            int currentPrice=stockPrices[i];

            if(!map.containsKey(currentPrice))
                map.put(currentPrice,i);

            if(currentPrice > maxPrice)
                maxPrice = currentPrice;

            System.out.println("On iteration: " + i);
            System.out.println("    currentPrice = " + currentPrice);
            System.out.println("    mimPrice = " + mimPrice);
            System.out.println("    maxPrice = " + maxPrice);
            System.out.println("    maxProfit = " + maxProfit);
            System.out.println("    map.get(mimPrice) = " + map.get(mimPrice));
            System.out.println("    map.get(maxPrice) = " + map.get(maxPrice));
            //if(map.get(mimPrice)< map.get(maxPrice)) {
                System.out.println("    Calculating MAX Profit from  maxProfit: " + maxPrice+ " - mimPrice: " + mimPrice + " = " + Integer.toString(maxPrice - mimPrice));
                maxProfit = Math.max(maxProfit, maxPrice - mimPrice);
                System.out.println("    New maxProfit = " + maxProfit);
                if(currentPrice < mimPrice)
                    mimPrice = currentPrice;
            //}

        }
        System.out.println("The MAX Profit(using Map) is = " + maxProfit);
        return maxProfit;
    }

    public static int getMaxProfitIter(int[] stockPrices) {

        if (stockPrices.length < 2) {
            throw new IllegalArgumentException("Getting a profit requires at least 2 prices");
        }

        // we'll greedily update minPrice and maxProfit, so we initialize
        // them to the first price and the first possible profit
        int minPrice = stockPrices[0];
        int maxProfit = stockPrices[1] - stockPrices[0];

        // start at the second (index 1) time
        // we can't sell at the first time, since we must buy first,
        // and we can't buy and sell at the same time!
        // if we started at index 0, we'd try to buy *and* sell at time 0.
        // this would give a profit of 0, which is a problem if our
        // maxProfit is supposed to be *negative*--we'd return 0.
        for (int i = 1; i < stockPrices.length; i++) {
            int currentPrice = stockPrices[i];

            // see what our profit would be if we bought at the
            // min price and sold at the current price
            int potentialProfit = currentPrice - minPrice;

            // update maxProfit if we can do better
            maxProfit = Math.max(maxProfit, potentialProfit);

            // update minPrice so it's always
            // the lowest price we've seen so far
            minPrice = Math.min(minPrice, currentPrice);
        }
        System.out.println("The MAX Profit is = " + maxProfit);
        return maxProfit;
    }


    public static void main(String[] args) {

        int[] stockPrices = new int[] {10,6,5,4,3,2,1};

        getMaxProfitMap(stockPrices);
        getMaxProfitIter(stockPrices);

    }

}
