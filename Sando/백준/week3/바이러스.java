package 백준.week3;

import java.util.*;
import java.io.*;

/**
 * Author    : Kang San Ah
 * Date      : 2025.04.27(Sun)
 * Runtime   : 1 sec
 * Memory    : 128 MB
 * Algorithm : DFS
 */

// https://www.acmicpc.net/problem/2606
public class 바이러스 {

    static int count, n, m, x, y;
    static List[] computers;
    static boolean [] visited;
    public static void dfs(int l){
        if (visited[l] == true) return;
        else{
            visited[l] = true;
            count ++;
            for (int i = 0 ; i < computers[l].size() ; i++){
                dfs((int)computers[l].get(i));
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        visited = new boolean[n+1];
        computers = new List[n+1];

        for (int i = 0 ; i < computers.length; i++){
            computers[i] = new ArrayList<>();
        }

        for (int i = 0 ; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
            computers[x].add(y);
            computers[y].add(x);
        }

        dfs(1);
        System.out.println(count-1);
    }
}