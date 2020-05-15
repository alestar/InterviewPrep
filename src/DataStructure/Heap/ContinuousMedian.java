package DataStructure.Heap;


import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

/**
 * Given an array of integers a[], return another array of median m[], where m[i] = median of a[0] through a[i]
 * median: middle in sorted order
 */

public class ContinuousMedian {

    private PriorityQueue<Integer> lowersMaxHeap;
    private PriorityQueue<Integer> uppersMinHeap;

    public PriorityQueue<Integer> getLowersMaxHeap() {
        return lowersMaxHeap;
    }

    public void setLowersMaxHeap(PriorityQueue<Integer> lowersMaxHeap) {
        this.lowersMaxHeap = lowersMaxHeap;
    }

    public PriorityQueue<Integer> getUppersMinHeap() {
        return uppersMinHeap;
    }

    public void setUppersMinHeap(PriorityQueue<Integer> uppersMinHeap) {
        this.uppersMinHeap = uppersMinHeap;
    }

    public double[] getMedians(int[] arr){

        lowersMaxHeap = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {//Change comparison to put bigger elements on the top
                return -1* a.compareTo(b);
            }
        });
        uppersMinHeap = new PriorityQueue<>();
        double[] medians = new double[arr.length];
        int number =-1;
        for (int i = 0; i < arr.length; i++) {
            number= arr[i];
            addNumber(number, lowersMaxHeap, uppersMinHeap);
            rebalance(lowersMaxHeap, uppersMinHeap);
            medians[i] = getMedian(lowersMaxHeap, uppersMinHeap);
        }
        return  medians;
    }

    private void addNumber(int number, PriorityQueue<Integer> lowersMaxHeap, PriorityQueue<Integer> uppersMinHeap) {
            if(lowersMaxHeap.isEmpty() || number < lowersMaxHeap.peek()){
                lowersMaxHeap.add(number);
            }
            else{
                uppersMinHeap.add(number);
            }
    }

    private void rebalance(PriorityQueue<Integer> lowersMaxHeap, PriorityQueue<Integer> uppersMinHeap) {
        PriorityQueue<Integer> biggerHeap =  lowersMaxHeap.size() > uppersMinHeap.size()? lowersMaxHeap: uppersMinHeap;
        PriorityQueue<Integer> smallerHeap = lowersMaxHeap.size() > uppersMinHeap.size()? uppersMinHeap: lowersMaxHeap;

        if(biggerHeap.size() - smallerHeap.size() >=2){// If is unbalance, then rebalance
            smallerHeap.add(biggerHeap.poll());
        }

    }

    private double getMedian(PriorityQueue<Integer> lowersMaxHeap, PriorityQueue<Integer> uppersMinHeap) {
        PriorityQueue<Integer> biggerHeap =  lowersMaxHeap.size() > uppersMinHeap.size()? lowersMaxHeap: uppersMinHeap;
        PriorityQueue<Integer> smallerHeap = lowersMaxHeap.size() > uppersMinHeap.size()? uppersMinHeap: lowersMaxHeap;

        if(biggerHeap.size() - smallerHeap.size() >=2 || biggerHeap.size() - smallerHeap.size() == 0){// If heaps are different size take both first elements and average them
             return ((double)biggerHeap.peek() + smallerHeap.peek()) / 2 ;
        }else{
          return biggerHeap.peek();// If size equal or diff by 1, return the first element of the bigger heap
        }
   }

    public static void main(String[] args) {

        ContinuousMedian cm = new ContinuousMedian();
        int[] arr = new int[20];
        for (int i = 1; i <= 5 ; i++) {// Fill up arr 0-4
            arr[i-1] = i;
        }
        System.out.println("numbers: " + Arrays.toString(arr) );
        System.out.println("medians: " + Arrays.toString(cm.getMedians(arr)) );
        System.out.println("lowerMaxHeap: " + cm.getLowersMaxHeap().toString());
        System.out.println("upperMinHeap: " + cm.getUppersMinHeap().toString());

        for (int i = 6; i <= 10 ; i++) { // Fill up arr 5-9
            arr[i-1] = i;
        }
        System.out.println("numbers: " + Arrays.toString(arr) );
        System.out.println("medians: " + Arrays.toString(cm.getMedians(arr)) );
        System.out.println("lowerMaxHeap: " + cm.getLowersMaxHeap().toString());
        System.out.println("upperMinHeap: " + cm.getUppersMinHeap().toString());

        for (int i = 11; i <= 15 ; i++) { // Fill up arr 10-14
            arr[i-1] = i;
        }
        System.out.println("numbers: " + Arrays.toString(arr) );
        System.out.println("medians: " + Arrays.toString(cm.getMedians(arr)) );
        System.out.println("lowerMaxHeap: " + cm.getLowersMaxHeap().toString());
        System.out.println("upperMinHeap: " + cm.getUppersMinHeap().toString());

        for (int i = 16; i <= 20 ; i++) { // Fill up arr 15-19
            arr[i-1] = i;
        }
        System.out.println("numbers: " + Arrays.toString(arr) );
        System.out.println("medians: " + Arrays.toString(cm.getMedians(arr)) );
        System.out.println("lowerMaxHeap: " + cm.getLowersMaxHeap().toString());
        System.out.println("upperMinHeap: " + cm.getUppersMinHeap().toString());
    }

}
