/**
 * Author    : Kang San Ah
 * Date      : 2025.05.15(Thu)
 * Runtime   : 1 sec
 * Memory    : 512 MB
 * Algorithm : DFS
 */

import java.io.*;
import java.util.*;

class Main {

    static int [] output;
    static int N, M;
    static StringBuilder sb;

    static void dfs(int depth){
        if(depth == M){
            for(int x : output){
                sb.append(x).append(' ');
            }
            sb.append('\n');
            return;
        }
        else{
            for(int i = 1; i <= N; i ++) {
                output[depth] = i;
                dfs(depth + 1);
            }
        }
    }

    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        output = new int[M];

        dfs(0);

        System.out.println(sb);
    }
}
