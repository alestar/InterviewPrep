package Java.DataStructure.LinkedList;

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


    public void printListNodeGeneric(){

        System.out.print("head: " + data + "->" + next.getData());
        LinkedListNodeGeneric<T> curr = next;
        while(curr.hasNext()) {
            System.out.print("->" + curr.getNext().getData());
            curr= curr.getNext();
        }
        System.out.println("");

    }

    public boolean hasNext(){
        return next!=null;
    }
}
