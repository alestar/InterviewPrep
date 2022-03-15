package MyJava.Problems.String;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

/**
 * Created by Alestar on 2/20/2019.
 */

public class WordCountEngine {

    public static String[][] wordCountEngine(String document) {
        // your code goes here
        //Normalize document to avoid capital letters
        document= document.toLowerCase();

        System.out.println("Document to normalize lower case");

        // Create Words Counts Map
        String[] splitedDoc= document.split(" ");
        HashMap<String,Integer> mapWordsCount = new HashMap<>();
        int largestCount= createCountsMap(splitedDoc, mapWordsCount);

        //Create Aux Ar rayOf Counts to Order Word Counts Map by Counts, in descending order
        List<String> arrOfCounts[] =createArrayOfCounts(mapWordsCount,largestCount);

        //List that maintains the original order for Single Counts words
        ArrayList<String> singleCountsListOrdered= createListOfSingleCountOrdered(splitedDoc, mapWordsCount);

        //Create wordCount
        String [][] wordCount = createWordCount(arrOfCounts, mapWordsCount.size(), singleCountsListOrdered);

        return wordCount;
    }

    public static  String[][] createWordCount(List<String> arrOfCounts[], int size, ArrayList<String> singleCountsListOrdered){
        String [][] wordCount = new String[size-1][2];
        int k = 0;
        for(int currentCounts=arrOfCounts.length-1 ; currentCounts>0; currentCounts--){
            List<String> listWords= new ArrayList<>();
            if(currentCounts == 1)
                listWords=singleCountsListOrdered;
            else
                listWords=arrOfCounts[currentCounts];

            for(String word: listWords) {
                if(word!= null) {
                    String[] pair = new String[]{word, Integer.toString(currentCounts)};
                    wordCount[k] = pair;
                    k++;
                }
            }
        }
        return wordCount;
    }

    public static ArrayList<String> createListOfSingleCountOrdered(String[] splitedDoc, HashMap<String,Integer> mapWordCounts){
         ArrayList<String> singleCountsList= new ArrayList<>();

        for (int i = 0; i < splitedDoc.length - 1; i++) {
            if(mapWordCounts.containsKey(splitedDoc[i]) &&  mapWordCounts.get(splitedDoc[i]) == 1){
                singleCountsList.add(splitedDoc[i]);
            }
        }
        return  singleCountsList;
    }

    public static List<String> [] createArrayOfCounts(HashMap<String, Integer> map, int size){
        List<String>[] arrOfListWordCounts = new List[size+1];


        for(String word: map.keySet()){
            Integer counts=map.get(word);
            if(arrOfListWordCounts[counts] == null) {
                List<String> list = new ArrayList<>();
                list.add(word);
                arrOfListWordCounts[counts]= list;
            }
            else
                arrOfListWordCounts[counts].add(word);
        }
        System.out.println(" Java.Problems.Array Of List Word Counts: " + Arrays.toString(arrOfListWordCounts));
        return arrOfListWordCounts;
    }

    public static int createCountsMap(String[] splittedDoc, HashMap<String, Integer> map){

        int largestCount = 0;
        for(int i=0; i< splittedDoc.length; i++){
            int count = 0;
            String w= splittedDoc[i];
            String word= purgeWord(w);

            if(map.containsKey(word)){
                count = map.get(word);
                count++;
                map.put(word, count);
            }
            else
                map.put(word, 1);

            if(count> largestCount)
                largestCount= count;
        }
        return largestCount;
    }

    public static String purgeWord(String w){
        char [] charArray=  w.toCharArray();
        StringBuilder sb = new StringBuilder();
        String word="";
        for(int c=0; c< charArray.length; c++){

            char current= charArray[c];
            if(current>='a' && current<='z')
                sb.append(current);
        }
        return  sb.toString();
    }

    public static void main(String[] args) {

        //Java.Problems.String document = "Practice makes perfect. you'll only get Perfect by practice. just practice!";
        String document = "Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!";
        String [][] wordCount= wordCountEngine(document);
        System.out.println("The word count output is: ");
        for (int i=0; i < wordCount.length; i++){
            System.out.println("The word count output is: " + Arrays.toString(wordCount[i]));


        }

    }


}
