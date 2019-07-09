package Matrix; /**
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
 * but only left or down.
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

            while((pawnLoc[1] < boardWidth) && ((pawnLoc[0]) < boardHeight)){
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
            3. right
        Recursive function to return how much grain can be collected by the rest of the moves from the given square
    */
    private static int ChessPawnRiceRecursive(int board[][], int memo[][], int m, int n, int x, int y) {
        // any other row, return the maximum of all 2 choices for move, plus the rice on this square
        if(memo[y][x] == -1)
            memo[y][x]= board[y][x];
        int down = (y < m-1 ? ChessPawnRiceRecursive(board, memo, m, n, x, y + 1) :0 );
        int right = (x < n - 1 ? ChessPawnRiceRecursive(board,memo, m, n, x + 1, y ) : 0);
        return memo[y][x] + Math.max(down, right);
    }
    public static void main(String[] args)
    {
        /*
        int board[][] = new int[][]{
                {1, 2, 1, 3, 4, 1, 1, 0},
                {1, 2, 2, 7, 1, 2, 1, 6},
                {1, 2, 1, 3, 4, 1, 1, 8},
                {1, 2, 2, 3, 1, 2, 1, 4},
                {1, 2, 1, 8, 4, 1, 1, 0},
                {1, 2, 2, 3, 1, 2, 1, 4},
                {1, 2, 1, 7, 4, 1, 1, 0},
                {1, 2, 2, 3, 1, 2, 1, 4}
                };

        */

        int board[][] = new int[][]{
                {2, 2, 4, 2},
                {0, 3, 0, 1,},
                {1, 2, 2, 1,},
                {4, 1, 2, 2,},

        };


        int m = board.length;
        int n = board[0].length;
        int[][] memo= new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                memo[i][j]= -1;
            }
        }

        int amountRecurv= ChessPawnRiceRecursive(board, memo,m,n,0,0);
        int amountItera= ChessPawnRiceIterative(board);
        System.out.println("The amount of rice from Recursive solution is: " + amountRecurv);
        System.out.println("The amount of rice from Iterative solution is: " + amountItera);
    }

}
