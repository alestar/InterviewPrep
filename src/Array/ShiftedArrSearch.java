package Array;

import java.util.*;
/**
  Input :
  3 4 5 1 2
  Value : 1
  Output : 3 (Index of value 1)

  Input :
  5 6 7 8 1 2 3 4
  Target : 7
  Output : 2   (Index of 7 in the array)

  Input :
  5, 6, 7, 0, 1, 2, 3, 4
  num 3

  1 2 3 4 5 6 7
*/
class ShiftedArrSearch {


  static int shiftedArrSearch(int[] shiftArr, int num) {
      
    //Binary Search for fiding the 'num' index
    int pIndex= findPivotPointIndex(shiftArr);
    if(pIndex== 0 || num< shiftArr[0])
    {
        return binarySearch(shiftArr,pIndex,shiftArr.length-1, num);
    }
    else
      return binarySearch(shiftArr,0,pIndex -1, num);
}
  
  static int findPivotPointIndex(int[] shiftArr){
     // Binary Search to find piv point
    int b=0;
    int e= shiftArr.length -1;
    int m=0;
    int p=-1;
    int prev=p-1;
    System.out.println("Finding pivot at array = " + Arrays.toString(shiftArr));
    while(b <= e){       
      m=(b + (e+1))/2;
        System.out.println("'b_index' = " + b + ", shiftArr[" + b + "]  = " + shiftArr[b] );
        System.out.println("'m_index' = " + m + ", shiftArr[" + m + "]  = " + shiftArr[m] );      
        System.out.println("'e_index' = " + e + ", shiftArr[" + e + "]  = " + shiftArr[e] );
        
      if(shiftArr[m] > shiftArr[b]){
          System.out.println("RIGHT half BECAUSE shiftArr[" + m + "] = " + shiftArr[m]);
          System.out.println(", MORE than shiftArr[" + b + "] = " + shiftArr[b] );        
          b=m + 1;// Select RIGHT half
          System.out.println("NEW 'b-index' = " + b + ", from 'm_index' = " + m + " + 1" );
       }
       else{
          System.out.println("LEFT half with BECAUSE shiftArr[" + m + "] = " + shiftArr[m]);
          System.out.println(", LESS than shiftArr[" + b + "] = " + shiftArr[b] );
          e=m - 1;  // Select LEFT half
          System.out.println("NEW 'e-index' = " + e + ", from 'm_index' = " + m + " - 1" );
       }      
        p=m;//Update p_index
      if(p==0)
        return p;
      else{
        prev= p-1;
        System.out.println("'p_index' = " + p + ", shiftArr[" + p + "]  = " + shiftArr[p] );      
        System.out.println("'prev_index' = " + prev + ", shiftArr[" + prev + "]  = " + shiftArr[prev] );
        if(shiftArr[p] < shiftArr[prev]){
            System.out.println(" FOUND 'p_index' = " + p + ", with value = " + shiftArr[p] );                               
            System.out.println("LESS than 'prev_index' = " + prev + ", with value = "  +shiftArr[prev]);
            return p; 
        }
      }
    }
    
    return 0;
  }
  
  static int binarySearch(int[] arr, int begin, int end, int target){
    int mid=0;
    while (begin <= end){
          mid=(begin + end)/2;
          if(arr[mid] == target){
           return mid;
          }
          else if(arr[mid] > target )
           end = mid - 1;//Pick LEFT half
          else
           begin = mid + 1;//Pick RIGHT half
    }
    return -1;
  }

  public static void main(String[] args) {
    int[] arrS= {9,12,17,2,4,5};
    int num= 17;
    int i = shiftedArrSearch(arrS, num);
      System.out.println(" FOUND ' num' = " + num + ", at index = " + i );


  }

}