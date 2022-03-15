package Java.Problems.RecursionAndDP;

import java.util.Arrays;

/**
 * @author Alestar
 *
 * Find a way to by k flavours of icecrem with m amount of money
 *
 * Rules:
 * Return indices of the array of flavours, not values (smaller indices first, meaning frist we found we take)
 * Only buy one of each flavor
 * Can't buy same item twice
 * Can't modify array
 */

public class IceCreamParlor {

    private static int indexOf(int[] menu, int value, int exclude) {
        for (int i = 0; i <menu.length ; i++) {
            if(menu[i] == value && i != exclude) {
                return i;
            }
        }
        return -1;
    }


    private static int[] getIndicesFromValues(int[] menu, int value1, int value2) {
        int index1 = indexOf (menu, value1, -1);
        int index2 = indexOf (menu, value2, index1);
        int[] indices= {Math.min(index1,index2), Math.max(index1,index2)};

        return indices;
    }



    public static int[] findChoices (int[] menu, int money) {
        int[] sortedMenu =menu.clone();
        Arrays.sort(sortedMenu);

        for (int i = 0; i < sortedMenu.length; i++) {
            int complement = money - sortedMenu[i];
            int location = Arrays.binarySearch(sortedMenu,i+1, sortedMenu.length, complement);

            if(location >= 0 && location < sortedMenu.length && sortedMenu[location] == complement){
                int[] indices = getIndicesFromValues(menu, sortedMenu[i], complement);
                return indices;
            }
        }
        return null;
    }



    public static void main(String[] args) {

        int[] prices1 ={1,9,5,4,2,6,5};
        int[] sorted1 =prices1.clone();
        Arrays.sort(sorted1);

        int[] princes2 ={2,7,13,5,4,13,5};
        int[] sorted2 =princes2.clone();
        Arrays.sort(sorted2);

        System.out.println("For array: " + Arrays.toString(prices1));
        System.out.println("    sorted: " + Arrays.toString(sorted1));
        System.out.println("    Found choices: " + Arrays.toString(findChoices(prices1, 10)));

        System.out.println("For array: " + Arrays.toString(princes2));
        System.out.println("    sorted: " + Arrays.toString(sorted2));
        System.out.println("    Found choices: " + Arrays.toString(findChoices(princes2, 10)));
    }
}
