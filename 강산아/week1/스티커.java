package week1;

import java.io.*;
import java.util.*;

/**
 * Author    : Kang San Ah
 * Date      : 2025.04.13(Sun)
 * Runtime   : 1 sec
 * Memory    : 256 MB
 * Algorithm : DP
 */

// https://www.acmicpc.net/problem/9465
public class 스티커 {

    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        for (int i = 1 ; i <= N ; i ++) {
            int t = Integer.parseInt(br.readLine());

            int[][] sticker = new int[2][t+1];

            for (int j = 0 ; j < 2 ; j ++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 1 ; k <= t ; k ++) {
                    sticker[j][k] = Integer.parseInt(st.nextToken());
                }
            }

            for(int p = 2 ; p <= t ; p ++) {
                sticker[0][p] += Math.max(sticker[1][p-1], sticker[1][p-2]);
                sticker[1][p] += Math.max(sticker[0][p-1], sticker[0][p-2]);
            }

            System.out.println(Math.max(sticker[0][t], sticker[1][t]));
        }
    }
}
