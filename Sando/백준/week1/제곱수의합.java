package 백준.week1;

/**
 * Author    : Kang San Ah
 * Date      : 2025.04.13(Sun)
 * Runtime   : 2 sec
 * Memory    : 128 MB
 * Algorithm : DP
 */

import java.io.*;
import java.util.*;

//https://www.acmicpc.net/problem/1699
public class 제곱수의합 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] dp = new int[N + 1];
        Arrays.fill(dp, 100000);

        for (int i = 1; i <= N; i++) {
            int k = (int) Math.sqrt(i);

            if (k * k == i) {
                dp[i] = 1;
            } else {
                for (int j = 1; j <= k; j++) {
                    dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
                }
            }
        }

        System.out.println(dp[N]); // 출력
    }
}
