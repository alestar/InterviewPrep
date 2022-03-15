package MyJava.Problems.String; /**
 * Created by Alestar on 2/20/2019.
 */
import java.util.*;

public class BracketValidator {

    public static char[][] TOKENS = {{'{','}'}, {'[', ']'}, {'(',')'}};

    public static boolean isOpenTerm(char c){
        for(char [] array: TOKENS) {
            if (array[0] == c){
                return true;
            }
        }
        return false; //If finishes loop without an open term match, it must not be an open term
    }
    public static boolean matches(char openTerm,char closeTerm){
        for(char [] array: TOKENS) {
            if (array[0] == openTerm) {
                return array[1] == closeTerm;
            }
        }
        return false; //If finishes loop without a match, there must not be any
    }

    public static boolean isBalanced(String expression){
        Stack<Character> stack = new Stack<Character>();
        for(char c: expression.toCharArray()) {
            if (isOpenTerm(c)) {
                stack.push(c);
            }else{
                if(stack.isEmpty() || !matches(stack.pop(), c)){
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }


    public static boolean isValid(String code) {

        Map<Character, Character> openersToClosers = new HashMap<>();
        openersToClosers.put('(', ')');
        openersToClosers.put('[', ']');
        openersToClosers.put('{', '}');

        Set<Character> openers = openersToClosers.keySet();
        Set<Character> closers = new HashSet<>(openersToClosers.values());

        Deque<Character> openersStack = new ArrayDeque<>();

        for (char c : code.toCharArray()) {
            if (openers.contains(c)) {
                openersStack.push(c);
            } else if (closers.contains(c)) {
                if (openersStack.isEmpty()) {
                    return false;
                } else {
                    char lastUnclosedOpener = openersStack.pop();

                    // if this closer doesn't correspond to the most recently
                    // seen unclosed opener, short-circuit, returning false
                    if (openersToClosers.get(lastUnclosedOpener) != c) {
                        return false;
                    }
                }
            }
        }
        return openersStack.isEmpty();
    }

    //{ [ ] ( ) }
    public static void main(String[] args) {
        String brackets1 = "{ [ ] ( ) }";
        String brackets3 = "{ } ( ) [ { } ]";
        String brackets5 = "[ ( { } ) ]";
        String brackets7 = "( { [ ] } ) ";
        String brackets2 = "{ [ }";
        String brackets4 = "[ ( { ) }]";
        String brackets6 = "( { [ } )";
        String brackets8 = "( ) } [ ]";


        String expressions1 = "{[]()}";
        String expressions3= "{}()[{}]";
        String expressions5 = "[({})]";
        String expressions7 = "({[]})";

        String expressions2 = "{[}";
        String expressions4 = "[({)}]";
        String expressions6 = "({[})";
        String expressions8 = "()}[]";

        //Valid Examples
        System.out.println("Valid example '" + brackets1 + "': " + isValid(brackets1));
        System.out.println("Valid example '" + brackets3 + "': " + isValid(brackets3));
        System.out.println("Valid example '" + brackets5 + "': " + isValid(brackets5));
        System.out.println("Valid example '" + brackets7 + "': " + isValid(brackets7));
        //Invalid Examples
        System.out.println("Invalid example '" + brackets2 + "': " + isValid(brackets2));
        System.out.println("Invalid example '" + brackets4 + "': " + isValid(brackets4));
        System.out.println("Invalid example '" + brackets6 + "': " + isValid(brackets6));
        System.out.println("Invalid example '" + brackets8 + "': " + isValid(brackets8));

        //Balanced Examples
        System.out.println("Balanced example '" + brackets1 + "': " + isBalanced(expressions1));
        System.out.println("Balanced example '" + brackets3 + "': " + isBalanced(expressions3));
        System.out.println("Balanced example '" + brackets5 + "': " + isBalanced(expressions5));
        System.out.println("Balanced example '" + brackets7 + "': " + isBalanced(expressions7));
        //Imbalanced Examples
        System.out.println("Imbalanced example '" + brackets2 + "': " + isBalanced(expressions2));
        System.out.println("Imbalanced example '" + brackets4 + "': " + isBalanced(expressions4));
        System.out.println("Imbalanced example '" + brackets6 + "': " + isBalanced(expressions6));
        System.out.println("Imbalanced example '" + brackets8 + "': " + isBalanced(expressions8));
    }


}
