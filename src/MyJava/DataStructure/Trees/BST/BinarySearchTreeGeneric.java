package MyJava.DataStructure.Trees.BST;

public class BinarySearchTreeGeneric<T extends  Comparable<T>> {

    BinaryTreeNodeGeneric<T> root;

    public void insert(T value){
        insertValue(root,value);
    }

    public void insertValue(BinaryTreeNodeGeneric node, T value){

        if(node == null)
            node =  new BinaryTreeNodeGeneric<>(value);

        if(node.getData().compareTo(value) < 0){
            if(node.getLeft() == null){
                node.setLeft(new BinaryTreeNodeGeneric<>(value));
            }
            else{
                insertValue(node.getLeft(),value);
            }
        }
        else {
            if (node.getRight() == null){
                node.setRight(new BinaryTreeNodeGeneric<>(value));
            }
            else{
                insertValue(node.getRight(),value);
            }

        }
    }

    public boolean contains(T value){
        return containsValue(root,value);
    }

    private boolean containsValue(BinaryTreeNodeGeneric<T> node, T value) {// Traverse Tree in PreOrder(root, left, right)
        if(node == null)
            return false;

        if(node.getData().compareTo(value) == 0)// Check Node
            return true;
        else if (node.getData().compareTo(value) >0){// Go left
             containsValue(node.getLeft(),value);
        }
        else{
            containsValue(node.getRight(),value);// Go right
        }
        return false; // if node is not null but all the comparison fail, return false
    }

    public void toString(BinaryTreeNodeGeneric<T> root) {// Traverse Tree InOrder(left, root, right)
        BinaryTreeNodeGeneric<T> curr = root;
        if (curr == null)
            return;
        else {
            toString(curr.getLeft());
            System.out.println(curr.toString());
            toString(curr.getRight());
        }
    }
}
