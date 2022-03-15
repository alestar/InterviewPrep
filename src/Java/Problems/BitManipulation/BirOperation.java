package Java.Problems.BitManipulation;

import java.util.Arrays;

public class BirOperation {

    public static boolean getElement(int number, int i){
        return (number&(1<<i)) !=0;
    }

    public static int setElement(int number, int i){
        return (number|(1<<i));
    }

    public static int clearElement(int number, int i){
        return (number&(~(1<<i)));
    }


    public static void main(String[] args) {

        int num1 =4; // Binary representation '100'
        int i1 =2;

        int num2 =8; // Binary representation '1000'
        int i2 =3;

        int num3 =10; // Binary representation '1010'
        int i3 =0;

        int num4 =11; // Binary representation '1011'
        int i4 =0;

        System.out.println("Is the ith bit position: '" + 2 + "' for number: '" + 4 + "' set? : " + getElement(4,2) );
        System.out.println("Is the ith bit position: '" + 3 + "' for number: '" + 8 + "' set? : " + getElement(8,3) );
        System.out.println("Is the ith bit position: '" + 0 + "' for number: '" + 10 + "' set? : " + getElement(10,0) );
        System.out.println("Is the ith bit position: '" + 0 + "' for number: '" + 11 + "' set? : " + getElement(11,0) );

        System.out.println("Setting the ith bit position: '" + 0 + "' for number: '" + 8 + "'  = " + setElement(8,0) ); // -> '9'
        System.out.println("Setting the ith bit position: '" + 0 + "' for number: '" + 10 + "'  = " + setElement(10,0) );// -> '11'
        System.out.println("Setting the ith bit position: '" + 1 + "' for number: '" + 4 + "'  = " + setElement(4,1) );// -> '6'
        System.out.println("Setting the ith bit position: '" + 0 + "' for number: '" + 12 + "'  = " + setElement(12,0) );// -> '13'

        System.out.println("Clearing the ith bit position: '" + 0 + "' for number: '" + 9 + "'  = " + clearElement(9,0) ); // -> '8'
        System.out.println("Clearing the ith bit position: '" + 0 + "' for number: '" + 11 + "'  = " + clearElement(11,0) );// -> '10'
        System.out.println("Clearing the ith bit position: '" + 1 + "' for number: '" + 6 + "'  = " + clearElement(6,1) );// -> '4'
        System.out.println("Clearing the ith bit position: '" + 0 + "' for number: '" + 13 + "'  = " + clearElement(13,0) );// -> '12'
    }
}
