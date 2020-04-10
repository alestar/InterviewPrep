package DataStructure.Trees.BST;

public class BinaryTreeNodeGeneric<T extends  Comparable<T>> {
    private T data;
    private BinaryTreeNodeGeneric left, right;

    public BinaryTreeNodeGeneric(T data) {
       this.data = data;
    }

    public void setData(T data) {
        this.data = data;
    }
    public T getData() {
        return data;
    }

    public void setLeft(BinaryTreeNodeGeneric left) {
        this.left = left;
    }
    public void setRight(BinaryTreeNodeGeneric right) {
        this.right = right;
    }

    public BinaryTreeNodeGeneric getLeft() {
        return left;
    }
    public BinaryTreeNodeGeneric getRight() {
        return right;
    }

    public String toString() {
        return data.toString()+" ";
    }
}
