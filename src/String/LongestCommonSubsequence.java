package String;

/**
 * Created by Alestar on 3/17/2019.
 */
public class LongestCommonSubsequence {

    /* Returns length of LCS for X[0..m-1], Y[0..n-1] */
    public static int lcsRecv( char[] X, char[] Y, int m, int n ){
        if (m == 0 || n == 0)
            return 0;
        if (X[m-1] == Y[n-1])
            return 1 + lcsRecv(X, Y, m-1, n-1);
        else
            return Math.max(lcsRecv(X, Y, m, n-1), lcsRecv(X, Y, m-1, n));
    }

    public static int lcsRecvMemo( char[] X, char[] Y, int m, int n , Integer [][] memo){
       if(memo[n-1][m-1] != null)
           return memo[n-1][m-1];
        int result=0;
        if (m == 0 || n == 0)
            return 0;
        if (X[m-1] == Y[n-1])
            result= 1 + lcsRecv(X, Y, m-1, n-1);
        else
            result= Math.max(lcsRecv(X, Y, m, n-1), lcsRecv(X, Y, m-1, n));
        memo[n-1][m-1]= result;
        return result;
    }
    public static void main(String[] args){
        LongestCommonSubsequence lcs = new LongestCommonSubsequence();
        //String s1 = "AGGTAB";
        //String s2 = "GXTXAYB";
        //Length of LCS is 4 -> "GTAB"

        String s1 = "ABCDGH";
        String s2 = "AEDFHR";
        //Length of LCS is 3 -> "ADH"

        char[] X=s1.toCharArray();
        char[] Y=s2.toCharArray();
        int m = X.length;
        int n = Y.length;
        Integer [][] memo = new Integer[n][m]; // {{null, null, null, null, null}, {...}, ...}

        System.out.println("Length of LCS (Recv) is" + " " +
                lcs.lcsRecv( X, Y, m, n ) );

        System.out.println("Length of LCS (Recv - Memo) is" + " " +
                lcs.lcsRecvMemo( X, Y, m, n, memo) );
    }

}
