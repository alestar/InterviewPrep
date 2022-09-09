package MyJava.DataStructure.Queue;

public class QueueGeneric<T> {

    private class Node<T>{
        private T data;
        private Node next;
        private Node (T data){
         data = data;
        }
    }
    private Node<T> head;// remove from the head
    private Node<T> tail;// add things at the end

    public boolean isEmpty(){
        return head == null;
    }

    public T peek(){
        return head.data;
    }

    public void add(T data){
        Node node = new Node(data);
        if(tail!=null){
            tail.next=node;
        }
        tail=node;
        if(head == null){
            head=node;
        }
    }
    public T remove(){

        T data= head.data;
        head = head.next;
        if(head == null){
            tail = null;
        }
        return data;
    }

}
