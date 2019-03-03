/**
 * Created by Alestar on 2/20/2019.
 */
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.NoSuchElementException;

public class QueueTwoStacks {

    private Deque<Integer> inStack = new ArrayDeque<>();
    private Deque<Integer> outStack = new ArrayDeque<>();

    public void enqueue(int item) {
        inStack.push(item);
    }

    public int dequeue() {
        if (outStack.isEmpty()) {

            // move items from inStack to outStack, reversing order
            while (!inStack.isEmpty()) {
                int newestInStackItem = inStack.pop();
                outStack.push(newestInStackItem);
            }

            // if outStack is still empty, raise an error
            if (outStack.isEmpty()) {
                throw new NoSuchElementException("Can't dequeue from empty queue!");
            }
        }
        return outStack.pop();
    }
}