package DataStructure.Trees.BST;

/**
 * Created by Alestar on 1/18/2019.
 */

public class SecondLargestInBST {

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

    public BinaryTreeNode createBinaryTreeNode(int value){
        return new BinaryTreeNode(value);
    }

    /** Given a binary tree, print its nodes in inorder*/
    void printInorder(BinaryTreeNode node, String dir)
    {
        if (node == null) {
            return;
        }

        if(node.left!=null) {/* first recur on left child */
            String d = "        Going Left <- ";
            printInorder(node.left, d);
        }

        /* then print the data of node */
        System.out.println("    " + dir + " Current NodeGeneric: " + node.toString() + ", ");

        if(node.right!=null) { /* now recur on right child */
            String d = "        Going Right -> ";
            printInorder(node.right, d);
        }
    }

    private static int findLargestRcurv(BinaryTreeNode rootNode) {
        if (rootNode == null) {
            throw new IllegalArgumentException("Tree must have at least 1 node");
        }
        if (rootNode.right != null)  {
            return findLargestRcurv(rootNode.right);
        }
        return rootNode.value;
    }

    public static int findSecondLargestRecurv(BinaryTreeNode rootNode) {

        if (rootNode == null || (rootNode.left == null
                && rootNode.right == null)) {
            throw new IllegalArgumentException("Tree must have at least 2 nodes");
        }

        // case: If we have a left subtree but not a right subtree, then the current node is the largest overall (the "rightmost") node.
        // The second largest element must be the largest element in the left subtree.
        // We use our findLargestRcurv() method above to find the largest in that left subtree!
        if (rootNode.left != null && rootNode.right == null) {
            return findLargestRcurv(rootNode.left);
        }

        // case: If we have a right child, but that right child node doesn't have any children,
        // then the right child must be the largest element and our current node must be the second largest element!
        if (rootNode.right != null && rootNode.right.left == null && rootNode.right.right == null) {
            return rootNode.value;
        }

        // otherwise: we have a right subtree with more than one element,
        // so the largest and second largest are somewhere in that subtree. So we step right.
        return findSecondLargestRecurv(rootNode.right);
    }

    private static int findLargestIter(BinaryTreeNode rootNode) {
        BinaryTreeNode current = rootNode;
        while (current.right != null) {
            current = current.right;
        }
        return current.value;
    }
    public static int findSecondLargestIter(BinaryTreeNode rootNode) {
        if (rootNode == null || (rootNode.left == null
                && rootNode.right == null)) {
            throw new IllegalArgumentException("Tree must have at least 2 nodes");
        }

        BinaryTreeNode current = rootNode;

        while (true) {

            // case: current is largest and has a left subtree
            // 2nd largest is the largest in that subtree
            if (current.left != null && current.right == null) {
                return findLargestIter(current.left);
            }

            // case: current is parent of largest, and largest has no children,
            // so current is 2nd largest
            if (current.right != null &&
                    current.right.left == null &&
                    current.right.right == null) {
                return current.value;
            }

            current = current.right;
        }
    }

    public static void main(String[] args) {
        SecondLargestInBST bt = new SecondLargestInBST();

        /**  Case: The largest node DOES NOT have a left subtree.
                 ( 5 )
                /     \
              (3)     (8)
             /  \     /  \
           (1)  (4) (7)  (9)

            Case: The largest node HAS a left subtree.
                ( 5 )
                /     \
             (3)     (8)
             /  \     /  \
         (1)  (4) (7)  (12)
                     /
                 (10)
                /  \
             (9)  (11)
         */
        BinaryTreeNode btn5= bt.createBinaryTreeNode(5);//Root
        //Left Tree
        BinaryTreeNode btn3= bt.createBinaryTreeNode(3);
        BinaryTreeNode btn1= bt.createBinaryTreeNode(1);
        BinaryTreeNode btn4= bt.createBinaryTreeNode(4);
        //Right Tree
        BinaryTreeNode btn8= bt.createBinaryTreeNode(8);
        BinaryTreeNode btn7= bt.createBinaryTreeNode(7);
        BinaryTreeNode btn12= bt.createBinaryTreeNode(12);
        //Left Sub-Tree
        BinaryTreeNode btn10= bt.createBinaryTreeNode(10);
        BinaryTreeNode btn9= bt.createBinaryTreeNode(9);
        BinaryTreeNode btn11= bt.createBinaryTreeNode(11);

        //Left Sub-Tree
        btn10.left= btn9;
        btn10.right= btn11;
        btn12.left=btn10;

        //Right Tree
        btn8.left= btn7;
        btn8.right= btn12;
        //Left Tree
        btn3.left=btn1;
        btn3.right=btn4;
        //Root
        btn5.left= btn3;
        btn5.right= btn8;
        bt.root=btn5;

        System.out.println(" The Balanced Binary Tree 'In-Order' ");
        bt.printInorder(bt.root, "Root: ");

        int secondLargestIter = bt.findSecondLargestIter(bt.root);
        int secondLargestRecurv = bt.findSecondLargestRecurv(bt.root);
        System.out.println(" The second largest value(Iter) is = " +  secondLargestIter);
        System.out.println(" The second largest value(Recursively) is = " +  secondLargestRecurv);
    }
}
