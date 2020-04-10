package DataStructure.LinkedList;

public class LinkedListGeneric<T> {

    private NodeGeneric<T> head;
    private int size = 0;

    public int size() {
        return size;
    }

    public NodeGeneric<T> head() {
        return head;
    }

    public T behead() {
        NodeGeneric<T> node = head;
        head=head.getNext();
        return node.getData();
    }

    public void insertWithData (T newData, T existData){

        NodeGeneric found = this.findWithData(existData);
        if(found!=null) {
            NodeGeneric newNode = new NodeGeneric(newData);
            newNode.setNext(found.getNext());
            found.setNext(newNode);
        }
        size++;
    }

    public void prepend(T data) {
        NodeGeneric newHead = new NodeGeneric(data);
        newHead.setNext(head);
        head= newHead;
        size++;
    }

    public void append(T data) {// Appending is O(n)

        NodeGeneric node = new NodeGeneric(data);
        if(head == null) {
            head = node;
            size++;
            return;
        }
        // Else traverse till the getLast node
        // and insert the new_node there
        NodeGeneric last = this.getLast();
        last.setNext(node);
        size++;
    }

    public void deleteWithValue(T data){
        if(head == null) return;
        if(head.getData() == data){
            head = head.getNext();
            return;
        }

        NodeGeneric found = this.findWithData(data);
        if(found!= null){
            found.setNext(found.getNext().getNext());
            return;
        }

    }

    public NodeGeneric findWithData(T data){
        NodeGeneric res= null;
        NodeGeneric current = head;
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

    public NodeGeneric getLast(){
        //Traverse till the getLast node
        NodeGeneric current = head;
        while (current.getNext() != null) {
            current= current.getNext();
        }
        return current;

    }

    public void pointLastToNode(T data){
        if(head == null)return;
        NodeGeneric last= getLast();
        NodeGeneric found= findWithData(data);
        if (last!= found)
            last.setNext(found);

    }

    @Override
    public String toString() {
        if(head == null)
            return "";

        String list = "[";
        NodeGeneric current = head;
        while (current.getNext() != null) {
            if(current.getData() != null)
                list+= current.getData().toString() + ", ";
            current= current.getNext();
        }
        list+= current.getData().toString()+ "]";
        return list ;
    }
}
