package 백준.week4;

/**
 * Author    : Kang San Ah
 * Date      : 2025.05.13(Tue)
 * Runtime   : 1 sec
 * Memory    : 512 MB
 * Algorithm : DFS
 */


import java.io.*;
import java.util.*;

class Main{

    static boolean[] visited;
    static int[] answer;
    static int N,M;

    public static void dfs(int L){
        if(L == M){
            for(int n : answer) {
                System.out.print(n + " ");
            }
            System.out.println();
            return;
        }else{
            for (int i = 1; i <= N; i++) {
                if (!visited[i]) {
                    visited[i] = true;
                    answer[L] = i;
                    dfs(L + 1);
                    visited[i] = false;
                }
            }
        }
    }

    public static void main(String[]args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        answer = new int [M];
        visited = new boolean[N+1];
        dfs(0);
    }
}
