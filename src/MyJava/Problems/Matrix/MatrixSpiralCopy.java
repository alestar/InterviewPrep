package MyJava.Problems.Matrix;

import java.util.Arrays;

/**
 * Created by Alestar on 2/18/2019.
 */
public class MatrixSpiralCopy {

    public static int[] spiralCopy(int[][] inputMatrix) {
        // your code goes here
        int numRows= inputMatrix.length;
        int numCols = inputMatrix[0].length;
        int total= inputMatrix[0].length * inputMatrix.length;

        if(total==0)
            return new int[0];

        int[] res= new int[total];
        int count=0;

        //Indexes
        int topRow= 0;
        int btmRow = numRows -1;
        int leftCol = 0;
        int rightCol= numCols-1;

        while (topRow <= btmRow && leftCol <= rightCol){

            // Copy the next top row (Increamenting col from left to right)
            for(int c=leftCol; c <= rightCol; c++){
                res[count]= inputMatrix[topRow][c];
                count++;
            }
            topRow++;// Done with that top row

            // Copy the next right hand side column (Increamenting row from top to bot)
            for(int r=topRow; r <= btmRow; r++){
                res[count]= inputMatrix[r][rightCol];
                count++;
            }
            rightCol--;// Done with that right col

            // Copy the next bottom row (Decreamenting col from right to left)
            if(topRow  <= btmRow){
                for(int c=rightCol; c >= leftCol; c--){
                    res[count]= inputMatrix[btmRow][c];
                    count++;
                }
                btmRow--; // Done with that btm row
            }

            // Copy the next bottom row (Decreamenting row from bot to to)
            if (leftCol <= rightCol){
                for(int r=btmRow; r >= topRow ; r--){
                    res[count]= inputMatrix[r][leftCol];
                    count++;
                }
                leftCol++;// Done with that left col
            }
        }
        return res;
    }

    public static void main(String[] args) {
        int matrix[][]  ={ {1,    2,   3,  4,    5},
                                {6,    7,   8,  9,   10},
                                {11,  12,  13,  14,  15},
                                {16,  17,  18,  19,  20} };
        //output: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]

        int[] res= spiralCopy(matrix);
        System.out.println("The spiral order is: " + Arrays.toString(res));
    }

}
