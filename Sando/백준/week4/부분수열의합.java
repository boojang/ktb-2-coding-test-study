package 백준.week4;

/**
 * Author    : Kang San Ah
 * Date      : 2025.05.15(Thu)
 * Runtime   : 1 sec
 * Memory    : 512 MB
 * Algorithm : DFS
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 부분수열의합 {
    static int count, N, M ;
    static int [] arr;

    static StringTokenizer st;

    static void dfs(int depth, int sum){
        if (depth == N) {
            if (sum == M){
                count++;
            }
            return;
        }
        else{
            dfs(depth+1, sum+arr[depth]);
            dfs(depth+1, sum);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < arr.length; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        count = 0;

        dfs(0, 0);

        if (M == 0) System.out.println(count-1);
        else System.out.println(count);
    }
}
