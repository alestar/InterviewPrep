package String; /**
 * Created by Alestar on 2/20/2019.
 */
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class BracketValidator {

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
        String brackets1= "{ [ ] ( ) }";
        String brackets2= "{ [ }";
        System.out.println("Valid example '{ [ ] ( ) }': " + isValid(brackets1));
        System.out.println("Invalid example '{ [ }': " + isValid(brackets2));
    }

}
