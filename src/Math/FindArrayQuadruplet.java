package Math;

import java.util.Arrays;

/**
 * Created by Alestar on 1/12/2019.
 */
public class FindArrayQuadruplet {

    static int[] findArrayQuadruplet(int[] arr, int s) {
        int n= arr.length;

        if(n<4)
            return new int[0];

        Arrays.sort(arr);
        int c=0, low=0, high=0;
        for(int i = 0; i <= n-4; i++) {
            for(int j = i+1; j <= n-3; j++) {
                c= s - (arr[i] + arr[j]);
                low= j+1;
                high= n-1;
                while(low < high){
                    if((arr[low] + arr[high]) < c){
                        low++;
                    }
                    else if((arr[low] + arr[high]) > c){
                        high--;
                    }
                    else{
                        return new int[]{arr[i], arr[j], arr[low], arr[high]};
                    }
                }
            }
        }
        return new int[0];
    }
}
