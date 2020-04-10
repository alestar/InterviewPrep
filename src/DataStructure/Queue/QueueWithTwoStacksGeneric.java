package DataStructure.Queue; /**
 * Created by Alestar on 2/20/2019.
 */
import java.util.*;

public class QueueWithTwoStacksGeneric<T> {

    private Stack<T> stackNewestOnTop = new Stack<T>();
    private Stack<T> stackOldestOnTop = new Stack<T>();

    public void enqueue(T value) {// Add item
        stackNewestOnTop.push(value);
    }

    public T peek(){// Get "oldest" item, meaning items at the beginning of the QueueGeneric
        //move elements from StackNewest to stackOldest
        shiftStacks();
        return stackOldestOnTop.peek();
    }
    public T dequeue() {// Get "oldest" item, meaning items at the beginning of the QueueGeneric
    //MOve elements froms tackNewest to stackOldest
        shiftStacks();
        return stackOldestOnTop.pop();

    }

    private void shiftStacks() {
        if(stackOldestOnTop.isEmpty()){
            while(!stackNewestOnTop.isEmpty()){
                stackOldestOnTop.push(stackNewestOnTop.pop());
            }
        }
    }

    @Override
    public String toString() {

       return stackNewestOnTop.toString() + stackOldestOnTop.toString();
    }
    public static void main(String[] args) {
        QueueWithTwoStacksGeneric q = new QueueWithTwoStacksGeneric();
        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        q.enqueue(4);
        q.enqueue(5);
        q.enqueue(6);
        q.enqueue(7);
        q.enqueue(8);
        q.enqueue(9);
        q.enqueue(10);;

        q.dequeue();//Remove '1'
        q.dequeue();//Remove '2'

        System.out.print("Current queue: " +  q.toString() );

    }


}