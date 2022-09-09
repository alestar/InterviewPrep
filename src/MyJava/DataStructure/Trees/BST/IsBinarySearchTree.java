package MyJava.DataStructure.Trees.BST;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * Created by Alestar on 1/18/2019.
 */

public class IsBinarySearchTree {

    BinaryTreeNode root;

    private class BinaryTreeNode {

        public int value;
        public BinaryTreeNode left;
        public BinaryTreeNode right;

        public BinaryTreeNode(int value) {
            this.value = value;
        }

        public BinaryTreeNode insertLeft(int leftValue) {
            this.left = new BinaryTreeNode(leftValue);
            return this.left;
        }

        public BinaryTreeNode insertRight(int rightValue) {
            this.right = new BinaryTreeNode(rightValue);
            return this.right;
        }

        @Override
        public String toString() {
            return "N{" + value + "}";
        }
    }

    private static class NodeBounds {

        BinaryTreeNode node;
        int lowerBound;
        int upperBound;

        NodeBounds(BinaryTreeNode node, int lowerBound, int upperBound) {
            this.node = node;
            this.lowerBound = lowerBound;
            this.upperBound = upperBound;
        }
    }

    public BinaryTreeNode createBinaryTreeNode(int value){
        return new BinaryTreeNode(value);
    }

    /** Given a binary tree, print its nodes in inorder*/
    void printInorder(BinaryTreeNode node, String dir){
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

    public static boolean isBinarySearchTreeRecur(BinaryTreeNode node) {

        if(node == null || (node.left == null && node.right == null))
            return true;

        if(node.value <= node.left.value || node.value >= node.right.value)
            return false;

        return isBinarySearchTreeRecur(node.left) && isBinarySearchTreeRecur(node.right);
    }

    public static boolean isBinarySearchTreeRecurUsingBounds(BinaryTreeNode node) {

        return isBinarySearchTreeBounds(node, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    private static boolean isBinarySearchTreeBounds(BinaryTreeNode node, int lowerBound, int upperBound) {
        if (node == null) {
            return true;
        }

        if (node.value >= upperBound || node.value <= lowerBound) {
            return false;
        }

        return isBinarySearchTreeBounds(node.left, lowerBound, node.value)
                && isBinarySearchTreeBounds(node.right, node.value, upperBound);
    }

    public static boolean isBinarySearchTreeStackUsingBounds(BinaryTreeNode root) {

        // start at the root, with an arbitrarily low lower bound
        // and an arbitrarily high upper bound
        Deque<NodeBounds> nodeAndBoundsStack = new ArrayDeque<>();
        nodeAndBoundsStack.push(new NodeBounds(root, Integer.MIN_VALUE, Integer.MAX_VALUE));

        // depth-first traversal
        while (!nodeAndBoundsStack.isEmpty()) {
            NodeBounds nb = nodeAndBoundsStack.pop();
            BinaryTreeNode node = nb.node;
            int lowerBound = nb.lowerBound;
            int upperBound = nb.upperBound;

            // if this node is invalid, we return false right away
            if (node.value <= lowerBound || node.value >= upperBound) {
                return false;
            }

            if (node.left != null) {
                // this node must be less (<=) than the current node
                nodeAndBoundsStack.push(new NodeBounds(node.left, lowerBound, node.value));
            }
            if (node.right != null) {
                // this node must be greater (>=) than the current node
                nodeAndBoundsStack.push(new NodeBounds(node.right, node.value, upperBound));
            }
        }

        // if none of the nodes were invalid, return true
        // (at this point we have checked all nodes)
        return true;
    }


    public static void main(String[] args) {
        IsBinarySearchTree bt = new IsBinarySearchTree();

        BinaryTreeNode btn1= bt.createBinaryTreeNode(50);// Root

        BinaryTreeNode btn2= bt.createBinaryTreeNode(30);// LinkedListNodeGeneric
        BinaryTreeNode btn4= bt.createBinaryTreeNode(20);// Child left
        BinaryTreeNode btn5= bt.createBinaryTreeNode(25);// Child right

        BinaryTreeNode btn3= bt.createBinaryTreeNode(80);// LinkedListNodeGeneric
        BinaryTreeNode btn6= bt.createBinaryTreeNode(70);// Child left
        BinaryTreeNode btn8= bt.createBinaryTreeNode(90);// Child Right

        btn3.right= btn8;
        btn3.left = btn6;
        btn2.right= btn5;
        btn2.left=btn4;
        btn1.right= btn3;
        btn1.left= btn2;
        bt.root=btn1;

        System.out.println(" The Balanced Binary Tree 'In-Order' ");
        bt.printInorder(bt.root, "Root: ");

        boolean resultRecv = bt.isBinarySearchTreeRecur(bt.root);
        boolean resultRecvBounds = isBinarySearchTreeRecurUsingBounds(bt.root);
        boolean resultStack = bt.isBinarySearchTreeStackUsingBounds(bt.root);

        System.out.println(" Is it a Binary Search  Tree (Recursively) ? : " +  resultRecv);
        System.out.println(" Is it a Binary Search  Tree (Recursively using Bounds) ? : " +  resultRecvBounds);
        System.out.println(" Is it a Binary Search  Tree (StackGeneric) ? : " +  resultStack);
    }
}
;