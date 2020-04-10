package Problems.NP;

import java.util.Arrays;

/**
 * Created by Alestar on 3/17/2019.
 */
public class KnapSack {

    private Integer [][] memo= null;
    private Integer [] weights= null;
    private Integer [] values= null;

    KnapSack(Integer [] weights, Integer [] values, int capacity){
        this.weights=weights;
        this.values= values;
        memo = new Integer[values.length+1][capacity+1];
    }

    public int ksRecv(int n, int capacity){
        int result =0;
        if(memo[n][capacity] !=  null)
            return memo[n][capacity];
        if(n==0 || capacity == 0)
            return 0;
        else if(this.weights[n] > capacity){
            result = ksRecv(n-1,capacity);
        }
        else {
            int valNoPick = ksRecv(n - 1, capacity);
            int valPick = ksRecv(n - 1, capacity - weights[n]);
            result = Math.max(valNoPick, valPick);
        }
        this.memo[n][capacity]= result;
        return result;

    }

    public static void main(String args[]){

        Integer weights[] = {-1,1,2,4,2,5};
        Integer values[] = {-1,5,3,5,3,2};
        int n = values.length-1;
        int capacity = 10;
        System.out.println("Input weights = " + Arrays.toString(weights) );
        System.out.println("Input values = " + Arrays.toString(values) );
        System.out.println("Input 'capacity' = " + capacity);

        KnapSack ks = new KnapSack(weights, values, capacity);
        int maxValue= ks.ksRecv(n, capacity);
        System.out.println("The max values is = " + maxValue);
    }

}
