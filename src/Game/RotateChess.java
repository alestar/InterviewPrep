package Game;

import java.util.Arrays;
import java.util.List;

/**
 John has always had trouble remembering chess game positions. To help himself with remembering, he decided to store game positions in strings. He came up with the following position notation:

 The notation is built for the current game position row by row from top to bottom, with '/' separating each row notation;
 Within each row, the contents of each square are described from the leftmost column to the rightmost;
 Each piece is identified by a single letter taken from the standard English names ('P' = pawn, 'N' = knight, 'B' = bishop, 'R' = rook, 'Q' = queen, 'K' = king);
 White pieces are designated using upper-case letters ("PNBRQK") while black pieces use lowercase ("pnbrqk");
 Empty squares are noted using digits 1 through 8 (the number of empty squares from the last piece);
 Empty lines are noted as "8".
 For example, for the initial position (shown in the picture below) the notation will look like this:

 "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

 After the white pawn moves from e2 to e4, the notation will be as follows:

 "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR"

 John has written down some positions using his notation, and now he wants to rotate the board 90 degrees clockwise and see what notation for the new board would look like. Help him with this task.

 Example

 For notation = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR", the output should be
 chessNotation(notation) = "RP4pr/NP4pn/BP4pb/QP4pq/K2P2pk/BP4pb/NP4pn/RP4pr".

 The notation corresponds to the initial position with one move made (white pawn from e2 to e4).
 After rotating the board, it will look like this:

 So, the notation of the new position is "RP4pr/NP4pn/BP4pb/QP4pq/K2P2pk/BP4pb/NP4pn/RP4pr".

 Input/Output

 [execution time limit] 3 seconds (java)

 [input] string notation

 Game position in John's notation. It is guaranteed that notation is correct, but not guaranteed that it represents a valid game position.

 Guaranteed constraints:
 15 ≤ notation.length ≤ 71.

 [output] string

 Notation for the position of the game board, rotated 90 degrees clockwise.

* */

public class RotateChess {

    public static String  chessNotation(String notation) {

        String chessNotation = "";

        String[] splittedNotation= notation.split("/");

        String r8= splittedNotation[splittedNotation.length-1]; //row = 8 index= 7
        List<String> r7= Arrays.asList(splittedNotation[splittedNotation.length-2]); //row = 7 index= 6
        List<String> r6= Arrays.asList(splittedNotation[splittedNotation.length-3]); //row = 6 index= 5
        List<String> r5= Arrays.asList(splittedNotation[splittedNotation.length-4]); //row = 5 index= 4
        List<String> r4= Arrays.asList(splittedNotation[splittedNotation.length-5]); //row = 4 index= 3
        List<String> r3= Arrays.asList(splittedNotation[splittedNotation.length-6]); //row = 3 index= 2
        List<String> r2= Arrays.asList(splittedNotation[splittedNotation.length-7]); //row = 2 index= 1
        List<String> r1= Arrays.asList(splittedNotation[splittedNotation.length-8]); //row = 1 index= 0

        int ir1 = 0, ir2 =0, ir3 = 0, ir4 = 0, ir5 = 0, ir6 = 0, ir7 = 0, ir8 = 0;
        int checkRowCount = 1;
        while(checkRowCount < 8){

            char c8= r8.charAt(ir8);



        }



    }

    // Driver program
    public static void main(String[] args)
    {
        String input = "kr3r/pp1nbppp/3p1n2/q1pPp1B1/4P1b1/2N2N2/PPP1BPPP/R2Q2RK";

        String output = RotateChess.chessNotation(input);

        System.out.println("The oputput of rotate chess is: " + output);
    }
}
