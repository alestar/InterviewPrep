package Problems.Matrix;

/**
 * Created by Alestar on 1/12/2019.
 */
public class NumberOfPathToDestInMatrixDiagonal {

    public static int Solution(int n) {
        // your code goes here
        if(n==0)
            return 0;

        // The memoization array is initialized with -1, to indicate uncalculated squares.
        int[][] memo= new int[n][n];
        for(int i=0; i < n; i++){
            for(int j=0; j < n; j++){
                memo[i][j]= -1;
            }
        }
        return findPaths(n-1,n-1,memo);
    }

    static int findPaths(int i, int j, int[][] memo){
        System.out.println("Checking 'i' = " + i + ", and 'j' = " + j );
        if(i < 0 || j < 0){//Passing the Start point outside of the board
            return 0;
        }
        else if(i<j){// Outside of Diagonal
            memo[i][j]= 0;
        }
        else if(memo[i][j] != -1){//If it's already computed, return the storage result (Memoization)
            return memo[i][j];
        }
        else if(i ==  0 && j == 0){//If reach goal return '1' path found
            memo[i][j]= 1;
        }
        else{
            memo[i][j]= findPaths(i-1 ,j, memo) + findPaths(i ,j-1, memo);// Add path(s) found recursively to memo
        }
        return  memo[i][j];

    }

    public static void main(String[] args) {
        int n= 3;
        int paths = Solution(n);
        System.out.println("Paths found for n = '" + n + "' : " + paths);
    }
}
