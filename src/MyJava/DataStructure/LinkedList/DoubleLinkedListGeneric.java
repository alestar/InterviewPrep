package MyJava.DataStructure.LinkedList;

public class DoubleLinkedListGeneric<T> {
    private class Node<T> {
        private T data;
        private Node next;
        private Node prev;

        private Node(T data) {
            data = data;
        }
    }
    private Node<T> head;

    public Node<T> getHead() {
          return head;
      }


    public void push(T data) {
        Node node = new Node(data);
        node.next=head.next;
        node.prev=head;
        head= node;

    }

    public T first() {
        Node<T> node = head;
        head=head.next;
        return node.data;
    }


    public void append(T data) {// Appending is O(n)
        {
            // Create a new node with given data
            Node node = new Node(data);

            // If the Linked List is empty,
            // then make the new node as head
            if (head == null) {
                head = node;
            } else {
                // Else traverse till the getLast node
                // and insert the new_node there
                Node last = head;
                while (last.next != null) {
                    last = last.next;
                }
                // Insert the new_node at getLast node
                last.next = node;
            }
        }
    }


}