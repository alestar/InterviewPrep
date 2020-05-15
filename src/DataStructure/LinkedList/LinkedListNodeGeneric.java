package DataStructure.LinkedList;

public class LinkedListNodeGeneric<T> {
    private T data;
    private LinkedListNodeGeneric next;

    public LinkedListNodeGeneric(T data) {
       this.data = data;
    }

    public T getData() {
        return data;
    }

    public LinkedListNodeGeneric getNext() {
        return next;
    }

    public void setData(T data) {
        this.data = data;
    }

    public void setNext(LinkedListNodeGeneric next) {
        this.next = next;
    }
}
