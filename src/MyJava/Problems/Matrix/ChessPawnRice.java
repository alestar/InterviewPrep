package MyJava.Problems.Matrix;

/**
 * Created by Alestar on 1/11/2019.
 */

/**
 * Originally taken as a timed coding test on Codility.com. This was one of two
 * problems that had to be solved in the space of 80 minutes. I completed the test
 * successfully, with correct answers for both exercises and plenty of time to spare
 *
 * Problem Definition:
 * There is a chess board of arbitrary number of rows and columns. On each square of the
 * board, a number of grains of rice have been placed. The arrangement of the squares,
 * including how many grains of rice are in each, is provided via the input array.
 *
 * A pawn, starts at the top left corner of the board. It can move one square at a time,
 * but only down or right.
 *
 * Write a program which returns the optimal path that the pawn must follow in order to collect
 * the maximum amount of grains of rice.
 */
public class ChessPawnRice {

    private static int ChessPawnRiceIterative(int[][] board) {
            int[] pawnLoc = {0,0};
            int totalGrains = 0;
            int totalRow = 0;
            int totalCol = 0;
            int boardWidth = board[0].length;
            int boardHeight = board.length;

            while((pawnLoc[1] < boardWidth) && ((pawnLoc[0]) < boardHeight)){//Check boundaries
                totalRow = 0;
                totalCol = 0;

                // add grains in current square
                totalGrains += board[pawnLoc[0]][pawnLoc[1]];

                // count the total grains in pawns untravelled column
                for(int i = pawnLoc[0]; i < board.length; i++){
                    totalCol += board[i][pawnLoc[1]];
                }

                // count the total grains in pawns untravelled row
                for(int i = pawnLoc[1]; i < board[0].length; i++){
                    totalRow += board[pawnLoc[0]][i];
                }

                if(totalRow > totalCol){ // move horizontally
                    pawnLoc[1] = pawnLoc[1] + 1;
                } else {                // move vertically
                    pawnLoc[0] = pawnLoc[0] + 1;
                }
            }

            return totalGrains;
        }

    /** Assuming that the pawn must begin at x=0,y=0 and there are three possible moves each time,
        problems doesn't describe the two types of moves possible, so we assume chess-like pawn moves:
            1. down,
            2. right
        Recursive function to return how much grain can be collected by the rest of the moves from the given square
    */
    private static int ChessPawnRiceRecursive(int board[][], int memo[][], int row, int col, int x, int y) {

        if(memo[y][x] == -1) // If is a new cell
            memo[y][x]= board[y][x];// Added top memo
        int down = (y < row-1 ? ChessPawnRiceRecursive(board, memo, row, col, x, y + 1) :0 );       //Move Down
        int right = (x < col - 1 ? ChessPawnRiceRecursive(board,memo, row, col, x + 1, y ) : 0);    // Move Right
        return memo[y][x] + Math.max(down, right);  // any other visited cell, return the maximum amount collected of the 2 choices for moving
                                                    // , plus the rice amount this cell
    }

    public static void resetMemo(int[][] memo, int row, int col){// Reset memo for the test, with all cell (-1)
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                memo[i][j]= -1;
            }
        }
    }

    public static void main(String[] args)
    {
        int board1[][] = new int[][]{
                {2, 2, 4, 2},
                {0, 3, 0, 1,},
                {1, 2, 2, 1,},
                {4, 1, 2, 2,},
        };

        int board2[][] = new int[][]{
                {1, 2, 1, 3, 4, 1, 1, 0},
                {1, 2, 2, 7, 1, 2, 1, 6},
                {1, 2, 1, 3, 4, 1, 1, 8},
                {1, 2, 2, 3, 1, 2, 1, 4},
                {1, 2, 1, 8, 4, 1, 1, 0},
                {1, 2, 2, 3, 1, 2, 1, 4},
                {1, 2, 1, 7, 4, 1, 1, 0},
                {1, 2, 2, 3, 1, 2, 1, 4}
         };

        //Prepare memo before colling method
        int row1 = board1.length;
        int col1 = board1[0].length;
        int[][] memo= new int[row1][col1];
        resetMemo(memo,row1,col1);

        int amountRecurv1= ChessPawnRiceRecursive(board1, memo,row1,col1,0,0);
        int amountItera1= ChessPawnRiceIterative(board1);
        System.out.println("For board1, the amount of MAX rice using Recursive solution is: " + amountRecurv1);
        System.out.println("For board1, the amount of MAX rice using Iterative solution is: " + amountItera1);

        //Prepare memo before colling method
        int row2 = board2.length;
        int col2 = board2[0].length;
        memo= new int[row2][col2];
        resetMemo(memo,row2,col2);

        int amountRecurv2= ChessPawnRiceRecursive(board2, memo,row2,col2,0,0);
        int amountItera2= ChessPawnRiceIterative(board2);
        System.out.println("For board2, the amount of MAX rice using Recursive solution is: " + amountRecurv2);
        System.out.println("For board2, the amount of MAX rice using Iterative solution is: " + amountItera2);
    }

}
