package week1;

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

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] dp = new int[11];

        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        for(int i = 4 ; i < 11 ; i ++) {
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
        }

        for(int i = 0 ; i < N ; i ++) {
            int num = Integer.parseInt(br.readLine());
            System.out.println(dp[num]);
        }
    }
}
