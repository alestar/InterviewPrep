package MyJava.DataStructure.LinkedList;

/**
 * Created by Alestar on 2/21/2019.
 */
public class KthToLastNodeInSinglyLinkedList {

    public static class LinkedListNode {

        public String value;
        public LinkedListNode next;

        public LinkedListNode(String value) {
            this.value = value;
        }

    }

    public static LinkedListNode kthToLastNode(int k, LinkedListNode head) {

        // STEP 1: get the length of the list
        // start at 1, not 0
        // else we'd fail to count the head node!
        int listLength = 1;
        LinkedListNode currentNode = head;

        // traverse the whole list,
        // counting all the nodes
        while (currentNode.next != null) {
            currentNode = currentNode.next;
            listLength += 1;
        }

        // STEP 2: walk to the target node
        // calculate how far to go, from the head,
        // to get to the kth to getLast node
        int howFarToGo = listLength - k;

        currentNode = head;
        for (int i = 0; i < howFarToGo; i++) {
            currentNode = currentNode.next;
        }

        return currentNode;
    }

    public static LinkedListNode kthToLastNodeUsingStick(int k, LinkedListNode head) {

        LinkedListNode leftNode  = head;
        LinkedListNode rightNode = head;

        // move rightNode to the kth node
        for (int i = 0; i < k - 1; i++) {
            rightNode = rightNode.next;
        }

        // starting with leftNode on the head,
        // move leftNode and rightNode down the list,
        // maintaining a distance of k between them,
        // until rightNode hits the end of the list
        while (rightNode.next != null) {
            leftNode  = leftNode.next;
            rightNode = rightNode.next;
        }

        // since leftNode is k nodes behind rightNode,
        // leftNode is now the at kth node from the last one of the list!
        return leftNode;
    }
    public static void main(String[] args) {

        LinkedListNode a = new LinkedListNode("Angel Food");
        LinkedListNode b = new LinkedListNode("Bundt");
        LinkedListNode c = new LinkedListNode("Cheese");
        LinkedListNode d = new LinkedListNode("Devil's Food");
        LinkedListNode e = new LinkedListNode("Eccles");

        a.next = b;
        b.next = c;
        c.next = d;
        d.next = e;

        System.out.println("The kth element to Last node is: " + kthToLastNode(2, a).value);
        System.out.println("The kth element to Last node (using Stick) is: " + kthToLastNodeUsingStick(2, a).value);
        // returns the node with value "Devil's Food" (the 2nd to getLast node)
    }

}
