// IMPORT LIBRARY PACKAGES NEEDED BY YOUR PROGRAM
import java.util.*;
// SOME CLASSES WITHIN A PACKAGE MAY BE RESTRICTED
// DEFINE ANY CLASS AND METHOD NEEDED
// CLASS BEGINS, THIS CLASS IS REQUIRED
public class CellsCompete
{
    // METHOD SIGNATURE BEGINS, THIS METHOD IS REQUIRED
    public List<Integer> cellCompete(int[] states, int days)
    {
        // WRITE YOUR CODE HERE
        int nextDay[]= new int[states.length];
        nextDay[0]=-1;

        //loop for each day
        for(int d=0; d < days; d ++){
            if(nextDay[0]!=-1){//Only fill up after the first time
                for(int i=0; i < nextDay.length; i++){//Update states with nextDay
                    states[i]= nextDay[i];
                }
            }

            for(int i=0; i < states.length; i++){

                if(i == 0 && states[i + 1] == 1){
                    nextDay[i]=1;
                }
                else if( i>0 && (i< states.length -1) && (states[i-1] != states[i+1])){
                    nextDay[i]=1;
                }
                else if(i == states.length -1 && states[i - 1] == 1){
                    nextDay[i]=1;
                }
                else{
                    nextDay[i]=0;
                }
            }
        }
        for(int i=0; i < nextDay.length; i++){//Update states with nextDay
            states[i]= nextDay[i];
        }

        List<Integer> list= new ArrayList<Integer>();
        for(int s: states){
            list.add(s);
        }
        return list;
    }
    // METHOD SIGNATURE ENDS
}
