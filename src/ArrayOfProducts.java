import java.util.Arrays;

/**
 * Created by Alestar on 2/20/2019.
 */
public class ArrayOfProducts {

    static int[] arrayOfArrayProducts(int[] arr) {
        // your code goes here
        int n = arr.length;

        if(n == 0 || n==1)
            return new int[0];

        //[2, 7, 3, 4,5,6]
        //2 =  1*  7 *3*4
        //7 = 2*      3*4*5*5
        //3 = 2*7     *4
        int [] prod= new int[n];

        //Left Side
        int product =1;
        for(int i=0; i<= n-1; i++){
            prod[i]= product;
            product *=arr[i];
        }
        //Right Side
        product=1;
        for(int i=n-1; i>=0; i--){
            prod[i]*= product;
            product *=arr[i];
        }
        return prod;
    }

    public static void main(String[] args) {
        int[] arr = {2, 7, 3, 4};//output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3]
        System.out.println("The array output is: " + Arrays.toString(arrayOfArrayProducts(arr)));
    }
}
