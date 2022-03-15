package MyJava.Problems.Math;

import java.util.ArrayList;
import java.util.List;

/**
 * Description
 * Write a function that given an integer N, returns the maximum possible value obtained by inserting one '5' digit inside the decimal representation of integer N.
 *
 * N is an integer within the range [-8000, 8000]
 *
 * Example1:
 * Input: N = 268
 * Output: 5268
 *
 * Example2:
 * Input: N = 670
 * Output: 6750
 *
 * Example3:
 * Input: N = 0
 * Output: 50
 *
 * Example4:
 * Input: N = -999
 * Output: -5999
 *
 * */

public class MaxPosibleValueWithFiveInsert {

    public static int maxPossibleValueWithMath(int N) {
        if (N == 0) {
            return 50;
        }
        List<Integer> list = new ArrayList<>();
        boolean isPositive = N > 0;
        N = Math.abs(N);
        while (N > 0) {
            list.add(N % 10);
            N /= 10;
        }
        int k = 0;
        boolean isAdded = false;
        for (int i = list.size() - 1; i >= 0; i--) {
            if (isPositive) {
                if (!isAdded && list.get(i) < 5) {
                    k = k * 10 + 5;
                    isAdded = true;
                }
            } else {
                if (!isAdded && list.get(i) > 5) {
                    k = k * 10 + 5;
                    isAdded = true;
                }
            }

            k = k * 10 + list.get(i);
        }
        if (!isAdded) {
            k = k * 10 + 5;
        }
        return k * (isPositive ? 1 : -1);
    }

    public static int maxPossibleValueWithString(int N) {
        int pos = 0;
        String number = String.valueOf(N);
        int firstNumber= Character.getNumericValue(number.charAt(0));
        int result = 0;

        if (N >= 0) {//If is positive

            //single digit
            if (number.length() == 1) {
                if (firstNumber > 5) {
                    return Integer.parseInt(number + "5");
                } else {
                    return Integer.parseInt("5" + number);
                }
            }
            //more than one digit
            for (char c : number.toCharArray()) {
                int digit = Character.getNumericValue(c);
                if (digit <= 5) {
                    result = Integer.parseInt(number.substring(0, pos) + 5 + number.substring(pos));
                } else{
                    result = Integer.parseInt(number.substring(0, pos) + 5 + number.substring(pos));
                }
                    pos++;
            }

        } else {
            String trimSign = number.substring(1);
            // System.out.println("** " + trimSign);
            for (char c : trimSign.toCharArray()) {

                int digit = Character.getNumericValue(c);

                if (digit >= 5 && pos == 0) {
                    result = Integer.parseInt("-5" + trimSign);
                } else if (digit < 5 && pos > 0) {
                    result = Integer.parseInt("-" + trimSign.substring(0, pos) + 5 + trimSign.substring(pos));
                } else if (digit < 5 && pos == 0) {
                    result = Integer.parseInt("-" + trimSign.substring(0, pos + 1) + 5 + trimSign.substring(pos + 1));
                }

                pos++;

            }
        }
        return result;
    }
    public static void main (String[] args)
    {
        int num= 63;
        System.out.println("Maximum Possible Value With Java.Problems.Math= " +  maxPossibleValueWithMath(num));
        System.out.println("Maximum Possible Value With Java.Problems.String = " +  maxPossibleValueWithString(num));
    }

}
