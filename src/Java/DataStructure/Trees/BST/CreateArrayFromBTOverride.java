package Java.DataStructure.Trees.BST; /**
 * Created by Alestar on 3/18/2019.
 */

import java.util.ArrayList;

/**
 * FB Python.Interview with (agrichuk )
 * Give a tree:
 *             1 -----> 1
 *            /\
 *           3  9    -----> 9
 *          /\   \
 *         4  5    10 -----> 10
 *          /     / \
 *         7     11  12  -----> 12
 *          \
 *           8 ---------------->8
 *
 *           Return arr[1,9,10,12,8]
 */

public class CreateArrayFromBTOverride {

    BinaryTreeNode root;

    public static class BinaryTreeNode {

        public int value;
        public BinaryTreeNode left;
        public BinaryTreeNode right;

        public BinaryTreeNode(int value) {
            this.value = value;
        }
        @Override
        public String toString() {
            return "N{" + value + "}";
        }
    }

    /** Given a binary tree, print its nodes in inorder*/
   public static void printInorder(BinaryTreeNode node, String dir) {
        if (node == null) {
            return;
        }

        if(node.left!=null) {/* first recur on left child */
            String d = "        Going Left <- ";
            printInorder(node.left, d);
        }

        /* then print the data of node */
        System.out.println("    " + dir + " Current LinkedListNodeGeneric: " + node.toString() + ", ");

        if(node.right!=null) { /* now recur on right child */
            String d = "        Going Right -> ";
            printInorder(node.right, d);
        }
    }

    public static ArrayList<Integer> addToArray(BinaryTreeNode root){

        ArrayList<Integer> arr = new ArrayList<Integer>();
        if (root == null)
            return arr;

        arr.add(root.value);
        traverseAddArr(root.left, arr,1);
        traverseAddArr(root.right, arr,1);
        return arr;
    }

    private static void traverseAddArr(BinaryTreeNode node, ArrayList<Integer> arr, int i){

        if(node == null)
            return;
        System.out.println("    current arr: " +  arr);
        if(i == arr.size())// To avoid IndexOutOfBound exception when initially filling up the arr
            arr.add(node.value);
        else
            arr.set(i,node.value);// Override the arr with the right sub-tree node 'blockers'
        i++;

        if(node.left != null)
            traverseAddArr(node.left,arr,i);  //Traverse tu left sub-tree
        if(node.right != null)
            traverseAddArr(node.right,arr,i);//Traverse tu right sub-tree


    }

    public static void main(String[] args) {

        BinaryTreeNode root = new BinaryTreeNode(1);
        BinaryTreeNode btn3= new BinaryTreeNode(3);
        BinaryTreeNode btn9= new BinaryTreeNode(9);

        BinaryTreeNode btn4= new BinaryTreeNode(4);
        BinaryTreeNode btn5= new BinaryTreeNode(5);

        BinaryTreeNode btn7= new BinaryTreeNode(7);
        BinaryTreeNode btn8= new BinaryTreeNode(8);

        BinaryTreeNode btn10= new BinaryTreeNode(10);
        BinaryTreeNode btn11= new BinaryTreeNode(11);
        BinaryTreeNode btn12= new BinaryTreeNode(12);

        //Right Sub-Tree
        btn10.left= btn11;
        btn10.right= btn12;
        btn9.right= btn10;

        //Left Sub-Tree
        btn7.right= btn8;
        btn5.left= btn7;
        btn3.left= btn4;
        btn3.right=btn5;

        //Root
        root.left = btn3;
        root.right = btn9;

        System.out.println(" The Balanced Binary Tree 'In-Order' ");
        printInorder(root, "Root: ");

        ArrayList<Integer> res = addToArray(root) ;
        System.out.println(" The array created from the tree looks like :" +  res);

    }
}
