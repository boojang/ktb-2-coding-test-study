package 백준.week1;

/**
 * Author    : Kang San Ah
 * Date      : 2025.04.12(Sat)
 * Runtime   : 1 sec
 * Memory    : 128 MB
 * Algorithm : DP
 */

import java.io.*;

// https://www.acmicpc.net/problem/1912
public class 연속합 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        int[] dp = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        dp[0] = arr[0];
        int max = dp[0];

        for (int i = 1; i < n; i++) {
            dp[i] = Math.max(arr[i], dp[i - 1] + arr[i]);
            max = Math.max(max, dp[i]);
        }

        System.out.println(max);
    }
}

