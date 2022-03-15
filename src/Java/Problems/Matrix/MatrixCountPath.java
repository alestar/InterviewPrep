package Java.Problems.Matrix;

public class MatrixCountPath {

    /**
     * Problem: Given two dimensional matrix, write an algorithm to count all possible paths from 'top left' corner to 'bottom-right' corner.
     * You are allowed to move only in two directions, move right OR move down.
     * <p>
     * Recursive Approach: From every cell you will have two options to make a move, either to go right OR down.
     * Base case will be check if you have reached to either last row OR last column,
     * then there is only one way to reach the last cell is to travel through that row or column.
     * <p>
     * Note: Time Complexity: It will be exponential: O(2^n^2) since we are solving many sub problems repeatedly.
     * However, using Memoization will decreased to O(n^2) quadratic.
     * <p>
     * Dynamic Bottom-up approach:
     */
    private static int countPaths(boolean[][] grid) {
        int[][] memo = new int[grid.length][grid[0].length];
        return countPaths(grid, 0, 0, memo);
    }

    private static int countPaths(boolean[][] grid, int row, int col, int[][] memo) {
        if (!isValid(grid, row, col)) return 0;
        if (isEnd(grid, row, col)) return 1;
        if (memo[row][col] == 0) {
            memo[row][col] = countPaths(grid, row + 1, col, memo) + countPaths(grid, row, col + 1, memo);
        }
        return memo[row][col];
    }

    private static boolean isEnd(boolean[][] grid, int row, int col) {
        if (row == grid.length - 1 && col == grid[0].length - 1) {
            return true;
        }
        return false;
    }

    private static boolean isValid(boolean[][] grid, int row, int col) {

        if (row >= grid.length || col >= grid[0].length || grid[row][col] == true) {
            return false;
        }
        return true;
    }

    public static int countPathDP(boolean[][] grid,  int start, int end) {

        int totalRow = grid.length;
        int totalCol = grid[0].length;

        int result[][] = new int[totalRow][totalCol];

        //base case: At the 'bottom-right' corner there is only one way to get to the end, staying there (convention).
        result[totalRow - 1][totalCol - 1] = 1;

        for (int i = 0; i <totalRow ; i++) {
            for (int j = 0; j <totalCol ; j++) {
                result[i][j] =-1;
            }
        }

        //At the last row, the number of paths to reach the end is always '1', because it can only move RIGHt. No UP, no LEFT, no DOWN.
        //Iterate through the last row ( decrementing each col) and assign '1' value, if is valid, if not assign '0'.
        for (int j = totalCol - 2; j >= 0; j--) {
            if (isValid(grid, totalRow - 1, j) && isValid(grid, totalRow - 1, j+1)) {
                result[totalRow - 1][j] = 1;
            } else
                result[totalRow - 1][j] = 0;
        }

        //At the last col, the number of paths to reach the end is always 1, because it can only move DOWN. No UP, no LEFT, no RIGHT.
        //Iterate through the last col ( decrementing each row) and assign '1' value if is valid, if not assign '0'.
        for (int i = totalRow - 2; i >= 0; i--) {
            if (isValid(grid, i, totalCol - 1) && isValid(grid, i+1, totalCol - 1)) {
                result[i][totalCol - 1] = 1;
            } else
                result[i][totalCol - 1] = 0;
        }

        //Now iterate through the rest of the cell from decrementing indices bottom-up and add path from moving DOWN and RIGHT to current cell
        //Start at the diagonal top-left cell from the 'end' cell, since is already establish that the end cell have value '1' (base case)
        for (int i = totalRow - 2; i >= 0; i--) {
            for (int j = totalCol - 2; j >= 0; j--) {
                if (isValid(grid, i, j)) {
                    result[i][j] =  result[i + 1][j] + result[i][j + 1];
                } else
                    result[i][j] = 0;
            }
        }
        return result[start][end];
    }

    public static void main(String[] args) {
        boolean grid1[][] = new boolean[][]{
                {false, false, false, false},
                {false, false, true, false},
                {true, false, false, false,},
                {false, true, false, false}
        };

        boolean grid2[][] = new boolean[][]{
                {false, false, false, false, false, false, false, false},
                {false, false, true, false, false, false, true, false},
                {false, false, false, false, true, false, false, false},
                {true, false, true, false, false, true, false, false},
                {false, false, true, false, false, false, false, false},
                {false, false, false, true, true, false, true, false},
                {false, true, false, false, false, true, false, false},
                {false, false, false, false, false, false, false, false}
        };

        System.out.println("Count Paths for 'grid1', to reach bottom-right from top left corner = " + countPaths(grid1));
        System.out.println("Count Paths for 'grid2', to reach bottom-right from top left corner= " + countPaths(grid2));

        System.out.println("Count Paths for 'grid1', to reach end from start (using DP)= " + countPathDP(grid1,0,0));
        System.out.println("Count Paths for 'grid2', to reach end from start (using DP)= " + countPathDP(grid2,0,0));
    }
}
