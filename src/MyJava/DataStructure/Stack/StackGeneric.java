package MyJava.DataStructure.Stack;

public class StackGeneric<T> {

    private class Node<T>{
        private T data;
        private Node next;
        private Node (T data){
            data = data;
        }
    }
    private Node<T> top;// remove from the head

    public boolean isEmpty(){
        return top == null;
    }
    public T peek(){
        return top.data;
    }
    public void push(T data){
        Node node = new Node(data);
        node.next=top;
        top=node;
    }
    public T pop(){
        T data= top.data;
        top = top.next;
        return data;
    }

}
