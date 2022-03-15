package Java.Problems.Game;

/**
 John has always had trouble remembering chess game positions. To help himself with remembering, he decided to store game positions in strings. He came up with the following position notation:

 The notation is built for the current game position row by row from top to bottom, with '/' separating each row notation;
 Within each row, the contents of each square are described from the leftmost column to the rightmost;
 Each piece is identified by a single letter taken from the standard English names ('P' = pawn, 'N' = knight, 'B' = bishop, 'R' = rook, 'Q' = queen, 'K' = king);
 White pieces are designated using upper-case letters ("PNBRQK") while black pieces use lowercase ("pnbrqk");
 Empty squares are noted using digits 1 through 8 (the number of empty squares from the getLast piece);
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

 Java.Problems.Game position in John's notation. It is guaranteed that notation is correct, but not guaranteed that it represents a valid game position.

 Guaranteed constraints:
 15 ≤ notation.length ≤ 71.

 [output] string

 Notation for the position of the game board, rotated 90 degrees clockwise.

* */

public class RotateChess {

    public static class Reference<T> {
        private T referent;

        public Reference(T initialValue) {
            referent = initialValue;
        }

        public void set(T newVal) {
            referent = newVal;
        }

        public T get() {
            return referent;
        }
    }

    public static String  chessNotation(String notation) {

        String[] splitdNotation= notation.split("/");

        char[] seg8= (splitdNotation[splitdNotation.length-1].toCharArray()); //row = 9 index= 7
        char[] seg7= (splitdNotation[splitdNotation.length-2].toCharArray()); //row = 8 index= 6
        char[] seg6= (splitdNotation[splitdNotation.length-3].toCharArray()); //row = 6 index= 5
        char[] seg5= (splitdNotation[splitdNotation.length-4].toCharArray()); //row = 5 index= 4
        char[] seg4= (splitdNotation[splitdNotation.length-5].toCharArray()); //row = 4 index= 3
        char[] seg3= (splitdNotation[splitdNotation.length-6].toCharArray()); //row = 3 index= 2
        char[] seg2= (splitdNotation[splitdNotation.length-7].toCharArray()); //row = 2 index= 1
        char[] seg1= (splitdNotation[splitdNotation.length-8].toCharArray()); //row = 1 index= 0

        Reference<Integer> index1 =  new Reference<>(0);
        Reference<Integer> index2 = new Reference<>(0);
        Reference<Integer> index3 = new Reference<>(0);
        Reference<Integer> index4 = new Reference<>(0);
        Reference<Integer> index5 = new Reference<>(0);
        Reference<Integer> index6 = new Reference<>(0);
        Reference<Integer> index7 = new Reference<>(0);
        Reference<Integer> index8 = new Reference<>(0);

        int checkRowCount = 0;
        StringBuilder result = new StringBuilder();
        while(checkRowCount < 8){

            StringBuilder newRow= new StringBuilder();
            Reference<Integer> carriedIncrement = new Reference<>(0);
            addCharToRow(newRow, seg8, index8, carriedIncrement);
            addCharToRow(newRow, seg7, index7, carriedIncrement);
            addCharToRow(newRow, seg6, index6, carriedIncrement);
            addCharToRow(newRow, seg5, index5, carriedIncrement);
            addCharToRow(newRow, seg4, index4, carriedIncrement);
            addCharToRow(newRow, seg3, index3, carriedIncrement);
            addCharToRow(newRow, seg2, index2, carriedIncrement);
            addCharToRow(newRow, seg1, index1, carriedIncrement);

            if(carriedIncrement.get() > 0) {// For any carried increment after the getLast segment is check
                newRow.append(carriedIncrement.get());
                carriedIncrement.set(0);
            }
            if(checkRowCount < 7) {
                newRow.append('/');
            }
            result.append(newRow.toString());
            checkRowCount++;
        }
         return result.toString();
    }

    static void addCharToRow(StringBuilder builder, char[] currentRow, Reference<Integer>  currRowIndex, Reference<Integer> addedNum){
        if(Character.isDigit(currentRow[currRowIndex.get()])) {
            Integer num= Character.getNumericValue(currentRow[currRowIndex.get()]);
            currentRow[currRowIndex.get()] = Character.forDigit(--num, 10);
            addedNum.set(addedNum.get() + 1);
            if(num == 0)
                currRowIndex.set(currRowIndex.get() +1);
        }else {
            if(addedNum.get() > 0) {
                builder.append(addedNum.get());
                addedNum.set(0);
            }
            builder.append(currentRow[currRowIndex.get()]);
            currRowIndex.set(currRowIndex.get() +1);
        }

    }

    // Driver program
    public static void main(String[] args)
    {
        String input = "2kr3r/pp1nbppp/3p1n2/q1pPp1B1/4P1b1/2N2N2/PPP1BPPP/R2Q2RK";
        String output = RotateChess.chessNotation(input);

        System.out.println("Input: 2kr3r/pp1nbppp/3p1n2/q1pPp1B1/4P1b1/2N2N2/PPP1BPPP/R2Q2RK");
        System.out.println("Expected: RP2q1p1/1P4p1/1PN1p2k/Q3Ppnr/1B1Pp1b1/1PN2np1/RP1bB1p1/KP4pr");
        System.out.println("Output: : " + output);
    }
}
