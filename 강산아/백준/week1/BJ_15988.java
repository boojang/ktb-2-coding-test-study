package 백준.week1;

import java.io.*;

/**
 * Author    : Kang San Ah
 * Date      : 2025.04.13(Sun)
 * Runtime   : 1 sec
 * Memory    : 512 MB
 * Algorithm : DP
 */

// https://www.acmicpc.net/problem/15988
public class BJ_15988 {

    static int MAX = 1000000;
    static int MOD = 1000000009;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        long[] dp = new long[MAX+1];

        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        for(int i = 4 ; i <= MAX ; i ++) {
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3] % MOD;
        }

        for(int i = 0 ; i < N ; i ++) {
            int num = Integer.parseInt(br.readLine());
            System.out.println(dp[num]);
        }
    }
}
