package MyJava.Algorithms.Search.DFS;

import java.util.Scanner;

// Tips:
// - Instead of using a "boolean[][] visited" array, we alter our original grid
// - Dont create a 2-D "Point" or "Cell" class. It's not necessary.

public class Connected_Cells_DFS {
   private static int rows; // here for convenience
   private static int cols; // here for convenience

    private static int findLargestRegion(int [][] matrix, int row, int col) {
        //Put boundary checks here (at top of recursive call), instead of before doing recursive call
        if ( matrix == null || row < 0 || row >= matrix.length || col < 0 || col >= matrix[row].length || matrix[row][col] == 0) {
            return 0;
        }

        matrix[row][col] = 0; // we alter the original matrix here
        int size = 1;       // 1 accounts for our size

        // Recursively search neighbors in ALL 8 directions
        for (int r = row - 1; r <= row + 1; r++) { // Move in all horizontal directions
            for (int c = col - 1; c <= col + 1; c++) {// Move in all vertical direction
                size += findLargestRegion(matrix, r, c);
            }
        }

        return size;
    }

   // Returns the size of the largest region
    public static int largestRegion(int [][] matrix) {
        int maxRegion = 0;

        for (int row = 0; row < matrix.length; row++) {//iterate through rows
            for (int col = 0; col < matrix[row].length; col++) {//iterate through cols
                /* Find the largest region from the current cell */
                if (matrix[row][col] == 1) {
                    int size  = findLargestRegion(matrix, row, col);
                    maxRegion = Math.max(maxRegion, size);
                }
            }
        }
        return maxRegion;
    }



    public static void main(String[] args) {
       // Save input grid
        Scanner scan = new Scanner(System.in);
        rows = scan.nextInt();
        cols = scan.nextInt();
        int [][] matrix = new int[rows][cols];
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                matrix[row][col] = scan.nextInt();
            }
        }
        scan.close();

        System.out.println(largestRegion(matrix));
    }
}