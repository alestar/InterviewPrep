package Java.DataStructure.LinkedList;

/**
 * Detect  a cycle in a linklist. Note that the head pointer maybe null if the list is empty.
 * Note: list can not be modified
 *  */
public class LinkedListHasCycle {


    public static boolean hasCycle(LinkedListGeneric linkedListGen) {

        LinkedListNodeGeneric head = linkedListGen.head();
        if (head == null) return false;

        LinkedListNodeGeneric fast = head.getNext();
        LinkedListNodeGeneric slow = head;
        while (fast != null && fast.getNext()!=null && slow != null) {
            if (fast == slow) {// When pointers collide , there is a loop in the Linked List
                return true;
            }
            fast = fast.getNext().getNext();
            slow = slow.getNext();
        }
        return false;
    }


    public static void main(String[] args) {

        LinkedListGeneric listGen = new LinkedListGeneric();
        listGen.append(1);
        listGen.append(2);
        listGen.append(3);
        listGen.append(4);
        listGen.append(5);

        System.out.println("ListGen size: [" + listGen.size() + "]");
        System.out.println("Checking ListGen: " + listGen.toString());

        listGen.pointLastToNode(2);
        System.out.println("  has a cycle [" + Boolean.toString(hasCycle(listGen)) + "]");
    }

}
