package DataStructure.Heap;

import java.util.Arrays;

public class MinHeap {

    private int capacity =10;
    private int size = 0;
    int [] items = new int[capacity];

    private int getLeftChildIndex(int parentIndex) {return 2 * parentIndex +1 ;}
    private int getRightChildIndex(int parentIndex) {return 2 * parentIndex + 2 ;}
    private int getParentIndex(int childIncex) {return (childIncex - 1)/2 ;}

    private boolean hasLeftChild (int index) { return getLeftChildIndex(index) < size; }
    private boolean hasRightChild (int index) { return getRightChildIndex(index) < size; }
    private boolean hasParent (int index) { return getParentIndex(index) >=0 ; }

    private int leftChild(int index){return items[getLeftChildIndex(index)];}
    private int rightChild(int index){return items[getRightChildIndex(index)];}
    private int parent(int index){return items[getParentIndex(index)];}

    private void swap(int indexOne, int indexTwo){
        int temp = items[indexOne];
        items[indexOne] = items[indexTwo];
        items[indexTwo] = temp;
    }

    private void ensureExtraCapacity(){
        if(size == capacity) {
            items = Arrays.copyOf(items, capacity * 2);
            capacity *= 2;
        }
    }

    public int peek(){
        if (size == 0) throw new IllegalStateException();
        return items[0];
    }

    public int poll(){
        if (size == 0) throw new IllegalStateException();
        int item =  items[0];
        items[0] = items[size -1];
        size--;
        adjustHeapDown();
        return item;
    }

    public void add(int item){
        ensureExtraCapacity();
        items[size]= item;
        size++;
        adjustHeapUp();
        
    }

    private void adjustHeapUp() {//heapifyUp()
    int index =size -1;
        while (hasParent(index)&& parent(index) > items[index]) {// Parents CAN NOT be bigger than childs in a minHeap, this mean out of order
                swap(getParentIndex(index),index);
                index = getParentIndex(index);
        }
    }

    private void adjustHeapDown() {// heapifyDown()
        int currIndex = 0;
        int smallerChildIndex = -1;
        while(hasLeftChild(currIndex)){// If there is NO left child, then certainly there is No right child
            smallerChildIndex= getLeftChildIndex(currIndex);
            if(hasRightChild(currIndex) && rightChild(currIndex)< leftChild(currIndex)){
                smallerChildIndex = getRightChildIndex(currIndex);
            }

            if(items[currIndex] <items[smallerChildIndex]){
                break;
            }
            else{
                swap(currIndex,smallerChildIndex);
            }
            currIndex = smallerChildIndex;
        }
    }
}
