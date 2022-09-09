package MyJava.DataStructure.Trees.BST; /**
 * Created by Alestar on 1/18/2019.
 */

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class BalancedBinaryTree {

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

    private static class NodeDepthPair {

        BinaryTreeNode node;
        int depth;

        NodeDepthPair(BinaryTreeNode node, int depth) {
            this.node = node;
            this.depth = depth;
        }

        @Override
        public String toString() {
            return "NodeDepthPair{" +
                    "node=" + node +
                    ", depth=" + depth +
                    '}';
        }
    }

    private BinaryTreeNode addRecursive(BinaryTreeNode current, int value) {
        if (current == null) {
            return new BinaryTreeNode(value);
        }
        if (current.left == null || value < current.value) {
            System.out.println("Adding LinkedListNodeGeneric to Left <- : " + current.toString() + ", ");
            return current.left = addRecursive(current.left, value);
        }
        else if (current.right == null || value > current.value) {
            System.out.println("Adding LinkedListNodeGeneric to Right -> : " + current.toString() + ", ");
            return current.right = addRecursive(current.right, value);
        }
        else {
            // value already exists
            return current;
        }
    }

    public void add(int value) {
        root = addRecursive(root, value);
    }

    public BinaryTreeNode createBinaryTreeNode(int value){
        return new BinaryTreeNode(value);
    }

    /** Given a binary tree, print its nodes according to the "bottom-up" postorder traversal. */
    void printPostorder(BinaryTreeNode node){
        if (node == null)
            return;

        // first recur on left subtree
        printPostorder(node.left);

        // then recur on right subtree
        printPostorder(node.right);

        // now deal with the node
        System.out.println("Current LinkedListNodeGeneric: " + node.toString() + ", ");
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

    /** Given a binary tree, print its nodes in preorder*/
    void printPreorder(BinaryTreeNode node){
        if (node == null)
            return;

        /* first print data of node */
        System.out.println("Current LinkedListNodeGeneric: " + node.toString() + ", ");

        /* then recur on left sutree */
        printPreorder(node.left);

        /* now recur on right subtree */
        printPreorder(node.right);
    }


    public boolean isBalanced(BinaryTreeNode treeRoot) {
        System.out.println("Determine if tree is balance?" );
        // a tree with no nodes is super balanced, since there are no leaves!
        if (treeRoot == null) {
            return true;
        }

        // we short-circuit as soon as we find more than 2
        List<Integer> depths = new ArrayList<>(3);

        Deque<NodeDepthPair> nodes = new ArrayDeque<>();//An StackGeneric
        nodes.push(new NodeDepthPair(treeRoot, 0));
        boolean balanced= true;
        while (!nodes.isEmpty() && balanced) {

            // pop a node and its depth from the top of our stack
            NodeDepthPair nodeDepthPair = nodes.pop();
            System.out.println("    Pop current: " + nodeDepthPair);
            BinaryTreeNode node = nodeDepthPair.node;
            int depth = nodeDepthPair.depth;

            // case: we found a leaf
            if (node.left == null && node.right == null) {
                System.out.println("        Current: " + nodeDepthPair + "has no children");

                // we only care if it's a new depth
                if (!depths.contains(depth)) {
                    System.out.println("        Adding depth = " + depth + ", from: " +  nodeDepthPair.toString());
                    depths.add(depth);
                    System.out.println("        Depths = " + depths.toString());

                    // two ways we might now have an unbalanced tree:
                    //   1) more than 2 different leaf depths
                    //   2) 2 leaf depths that are more than 1 apart
                    if (depths.size() > 2){
                        System.out.println("            Found depths > 2 = " + depths.size());
                        balanced= false;
                    }
                    if(depths.size() == 2 && Math.abs(depths.get(0) - depths.get(1)) > 1) {
                        System.out.println("            Found depths == 2 but diff > 1 =  " + Integer.toString( Math.abs(depths.get(0) - depths.get(1))));
                        balanced= false;
                    }
                }

                // case: this isn't a leaf - keep stepping down
            } else {
                if (node.right != null) {
                    NodeDepthPair rightNodeDepthPair= new NodeDepthPair(node.right, depth + 1);
                    nodes.push(rightNodeDepthPair);
                    System.out.println("        Pushed new DepthNodePair 'Right' = " + rightNodeDepthPair.toString());
                }
                if (node.left != null) {
                    NodeDepthPair leftNodeDepthPair= new NodeDepthPair(node.left, depth + 1);
                    nodes.push(leftNodeDepthPair);
                    System.out.println("        Pushed new DepthNodePair 'Left' = " + leftNodeDepthPair.toString());
                }
            }
        }

        return balanced;
    }

    public static void main(String[] args) {
        BalancedBinaryTree bt = new BalancedBinaryTree();

        BinaryTreeNode btn1= bt.createBinaryTreeNode(1);
        BinaryTreeNode btn2= bt.createBinaryTreeNode(2);
        BinaryTreeNode btn3= bt.createBinaryTreeNode(3);
        BinaryTreeNode btn4= bt.createBinaryTreeNode(4);
        BinaryTreeNode btn5= bt.createBinaryTreeNode(5);

        btn4.left= btn5;
        btn2.right=btn4;
        btn1.left= btn2;
        btn1.right= btn3;
        bt.root=btn1;

        System.out.println(" The Balanced Binary Tree 'In-Order' ");
        bt.printInorder(bt.root, "Root: ");

        boolean r=bt.isBalanced(bt.root);
        System.out.println(" Is Balanced Binary Tree 'balanced'? : " +  r);

    }
}
