package Problems.Math.Overlap;

/**
 * Created by Alestar on 1/12/2019.
 */
public class MeetingPlanner {

    static int[] Solution(int[][] slotsA, int[][] slotsB, int dur) {
        // your code goes here

        int indexA=0;
        int indexB=0;
        int stA=0;
        int etA=0;
        int stB=0;
        int etB=0;

        while(indexA < slotsA.length && indexB <slotsB.length){

            stA= slotsA[indexA][0];
            etA= slotsA[indexA][1];
            stB= slotsB[indexB][0];
            etB= slotsB[indexB][1];
            //{10,50}
            if(etA-stA < dur) {
                indexA++;
                continue;
            }
            //{0,15}
            if(etB-stB < dur){
                indexB++;
                continue;
            }
            //10 15
            if(stA < etB && stA>=stB){
                if(stA + dur <= etB ){
                    return new int[]{stA,stA + dur};
                }
            }
            //{0 50 10}
            else if(stB < etA && stB>=stA){
                if(stB + dur <= etA ){
                    return new int[]{stB,stB + dur};
                }
            }
            //15 < 50
            if(etA<etB)
                indexA++;
            else
                indexB++;

        }

        return new int[0];
    }

}
