package MyJava.DataStructure.LinkedList;

import java.util.LinkedList;

public class AddTwoNumLinkedList {

    public static LinkedListNodeGeneric<Integer> addTwoNumbersLinked(LinkedListNodeGeneric<Integer> l1, LinkedListNodeGeneric<Integer> l2){
        return addTwoNumbersLinkedListRecurv(l1,l2,0);
    }

    public static LinkedListNodeGeneric<Integer> addTwoNumbersLinkedListRecurv(LinkedListNodeGeneric<Integer> l1,LinkedListNodeGeneric<Integer> l2, int c){
        //Calculate value to add to the current node
        int val =  l1.getData() + l2.getData() + c;
        c = val / 10; // Dividing by '10' will retrieve the result of the div and will only be = 1 when val >= 10, because 10 fit only '1' time inside 'val', therefore that value 'c' = '1' should be carry over to the next sum of digits, otherwise 'c' = '0'
        int m= val % 10; // Modding by '10' will retrieve the rest of the division and will only give value '0' when 'val' = 10, otherwise will return the 'first digit' of 'val' (i.e 'val' = '14', 'm' = '4').
        LinkedListNodeGeneric<Integer> res = new LinkedListNodeGeneric<>(m);// Add the modded value to that digit

        //Move to the next node
        if(l1.hasNext() || l2.hasNext()){
            if(!l1.hasNext())//If there are no more nodes to keep adding for one of the numb list
                l1.setNext(new LinkedListNodeGeneric(0)); //Add a '0' to the sum to consider the other number when adding diff length numbers
            if(!l2.hasNext())//If there are no more nodes to keep adding for one of the numb list
                l2.setNext(new LinkedListNodeGeneric(0)); //Add a '0' to the sum to consider the other number when adding diff length numbers
            res.setNext(addTwoNumbersLinkedListRecurv(l1.getNext(),l2.getNext(),c)); //Proceed to add the next number with the carry over
        }
        else if (c >0)//If there are no more numbers to add, conditionally add the carry over 'c' if > 0
            res.setNext( new LinkedListNodeGeneric(c));

        return res;

    }


    public static LinkedListNodeGeneric<Integer> addTwoNumbersLinkedListIter(LinkedListNodeGeneric<Integer> l1,LinkedListNodeGeneric<Integer> l2){
        int val = 0 , c = 0, m = 0;
        LinkedListNodeGeneric<Integer> a = l1;
        LinkedListNodeGeneric<Integer> b = l2;
        LinkedListNodeGeneric<Integer> res = null;
        LinkedListNodeGeneric<Integer> curr = null;

        while (a!= null || b!=null){
            val = a.getData() + b.getData() + c;
            c= val/10;
            m= val % 10;

            if(curr == null) {
             curr = new LinkedListNodeGeneric<>(m);
             res = curr;
            }
            else {
                curr.setNext( new LinkedListNodeGeneric<>(m));
                curr= curr.getNext();
            }

            //Guarantee that if next node does not have a number is set to '0' to make addition possible
            if(a.hasNext() || b.hasNext()) {
                if (!a.hasNext())//If there are no more nodes to keep adding for one of the numb list
                    a.setNext(new LinkedListNodeGeneric(0)); //Add a '0' to the sum to consider the other number when adding diff length numbers
                if (!b.hasNext())//If there are no more nodes to keep adding for one of the numb list
                    b.setNext(new LinkedListNodeGeneric(0)); //Add a '0' to the sum to consider the other number when adding diff length numberselse if (c >0)
            }
            else if (c >0) {
                curr.setNext(new LinkedListNodeGeneric<>(c));
            }
            //Move to the next node
            a= a.getNext();
            b= b.getNext();
        }
        return res;
    }

    public static void main(String[] args) {

        LinkedListNodeGeneric<Integer> l1 = new LinkedListNodeGeneric<>(2);
        l1.setNext(new LinkedListNodeGeneric(4));
        l1.getNext().setNext(new LinkedListNodeGeneric(3));

        LinkedListNodeGeneric<Integer> l2 = new LinkedListNodeGeneric<>(5);
        l2.setNext(new LinkedListNodeGeneric(6));
        l2.getNext().setNext(new LinkedListNodeGeneric(4));

        LinkedListNodeGeneric<Integer> restRcrv =  addTwoNumbersLinked(l1,l2);
        System.out.println("Printing result using recursion: ");
        restRcrv.printListNodeGeneric();

        LinkedListNodeGeneric resIter =  addTwoNumbersLinkedListIter(l1,l2);
        System.out.println("Printing result using iteration: ");
        resIter.printListNodeGeneric();
    }

}
