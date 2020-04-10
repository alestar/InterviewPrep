package DataStructure.LinkedList;

public class NodeGeneric<T> {
    private T data;
    private NodeGeneric next;

    public NodeGeneric(T data) {
       this.data = data;
    }

    public T getData() {
        return data;
    }

    public NodeGeneric getNext() {
        return next;
    }

    public void setData(T data) {
        this.data = data;
    }

    public void setNext(NodeGeneric next) {
        this.next = next;
    }
}
