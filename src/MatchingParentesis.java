/**
 * Created by Alestar on 2/21/2019.
 */
public class MatchingParentesis {

    public static int getClosingParen(String sentence, int openingParenIndex) {
        int openNestedParens = 0;

        for (int position = openingParenIndex + 1; position < sentence.length(); position++) {
            char c = sentence.charAt(position);

            if (c == '(') {
                openNestedParens++;
            } else if (c == ')') {
                if (openNestedParens == 0) {
                    return position;
                } else {
                    openNestedParens--;
                }
            }
        }

        throw new IllegalArgumentException("No closing parenthesis :(");
    }
    public static void main(String[] args) {
        String sentence= "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.";
        System.out.println("Closing parenthesis is at: " + getClosingParen(sentence, 10));
    }
}
