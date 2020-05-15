package DataStructure.LinkedList;

public class LinkedListGeneric<T> {

    private LinkedListNodeGeneric<T> head;
    private int size = 0;

    public int size() {
        return size;
    }

    public LinkedListNodeGeneric<T> head() {
        return head;
    }

    public T behead() {
        LinkedListNodeGeneric<T> node = head;
        head=head.getNext();
        return node.getData();
    }

    public void insertWithData (T newData, T existData){

        LinkedListNodeGeneric found = this.findWithData(existData);
        if(found!=null) {
            LinkedListNodeGeneric newNode = new LinkedListNodeGeneric(newData);
            newNode.setNext(found.getNext());
            found.setNext(newNode);
        }
        size++;
    }

    public void prepend(T data) {
        LinkedListNodeGeneric newHead = new LinkedListNodeGeneric(data);
        newHead.setNext(head);
        head= newHead;
        size++;
    }

    public void append(T data) {// Appending is O(n)

        LinkedListNodeGeneric node = new LinkedListNodeGeneric(data);
        if(head == null) {
            head = node;
            size++;
            return;
        }
        // Else traverse till the getLast node
        // and insert the new_node there
        LinkedListNodeGeneric last = this.getLast();
        last.setNext(node);
        size++;
    }

    public void deleteWithValue(T data){
        if(head == null) return;
        if(head.getData() == data){
            head = head.getNext();
            return;
        }

        LinkedListNodeGeneric found = this.findWithData(data);
        if(found!= null){
            found.setNext(found.getNext().getNext());
            return;
        }

    }

    public LinkedListNodeGeneric findWithData(T data){
        LinkedListNodeGeneric res= null;
        LinkedListNodeGeneric current = head;
        while (current.getNext() != null) {
            if (current.getData() == data) {
               break;
            }
            current= current.getNext();
        }
        if(current!=null)// current can traverse to the end and return the 'last' node as found with with param:<data>, without actually ever finding the <node> with respective <data>
            res=current;
        return res;
    }

    public LinkedListNodeGeneric getLast(){
        //Traverse till the getLast node
        LinkedListNodeGeneric current = head;
        while (current.getNext() != null) {
            current= current.getNext();
        }
        return current;

    }

    public void pointLastToNode(T data){
        if(head == null)return;
        LinkedListNodeGeneric last= getLast();
        LinkedListNodeGeneric found= findWithData(data);
        if (last!= found)
            last.setNext(found);

    }

    @Override
    public String toString() {
        if(head == null)
            return "";

        String list = "[";
        LinkedListNodeGeneric current = head;
        while (current.getNext() != null) {
            if(current.getData() != null)
                list+= current.getData().toString() + ", ";
            current= current.getNext();
        }
        list+= current.getData().toString()+ "]";
        return list ;
    }
}
