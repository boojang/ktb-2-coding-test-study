package week1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * Author    : Kang San Ah
 * Date      : 2025.04.07(Mon)
 * Runtime   : 1 sec
 * Memory    : 256 MB
 * Algorithm : DFS
 */


public class N과M12 {

    static int N, M;
    static int[] arr, result;
    static StringBuilder sb;

    public static void dfs(int L, int start) {
        if (L == M) {
            for (int i = 0; i < M; i++) {
                sb.append(result[i]).append(' ');
            }
            sb.append('\n');
            return;
        }

        int before = -1;
        for (int i = start; i < N; i++) {
            if (before == arr[i]) continue;
            result[L] = arr[i];
            before = arr[i];
            dfs(L + 1, i);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N];
        result = new int[M];

        st = new StringTokenizer(br.readLine());
        sb = new StringBuilder();

        for (int i = 0; i < N; i++) arr[i] = Integer.parseInt(st.nextToken());

        Arrays.sort(arr);
        dfs(0, 0);

        System.out.print(sb);
    }
}
