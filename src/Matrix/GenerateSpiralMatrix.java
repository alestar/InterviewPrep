package Matrix;

import java.util.Arrays;

/**
 * Created by Alestar on 3/17/2019.
 */
public class GenerateSpiralMatrix {

    public static int[][] genSpiral(int n) {
        if (n<=0) {
            throw new IllegalArgumentException("N must be >0");
        }
        int[] dc = new int[]{1,0,-1,0};
        int[] dr = new int[]{0,1,0,-1};
        int dir = 0, val=0, r=0, c=0,limit=n*n;
        int[][] matrix = new int[n][n];
        while (val++ < limit) {
            matrix[r][c] = val;
            r += dr[dir];
            c += dc[dir];
            if (isInvalid(matrix,r, c)) {
                r-= dr[dir];
                c-=dc[dir];
                dir = (dir+1)%4;

                r+= dr[dir];
                c+= dc[dir];
                System.out.println("Update 'dir' to = " + dir);
                System.out.println("Update 'r' to = " + r);
                System.out.println("Update 'c' to = " + c);
            }
        }
        return matrix;
    }
    private static boolean isInvalid(int[][] m, int r, int c) {
        return r<0||c<0||r>=m.length||c>= m.length||m[r][c] != 0;
    }

    public static void main(String args[]){
        int n= 3;
        System.out.println("Input 'n' = " + n);
        int res[][]= genSpiral(n);
        System.out.println("Total Number of Subsets found= " + Arrays.deepToString(res));
    }

}
