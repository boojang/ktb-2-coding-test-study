package 백준.week3;

import java.io.*;
import java.util.*;

public class 숨바꼭질4 {

    static int MAX = 10001;

    static StringTokenizer st;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        Queue<Integer> q = new LinkedList<>();

        int [] parent = new int[MAX]; // 1촌, 2촌, 3촌 느낌
        int [] visited = new int[MAX]; // 몇 번만에 방문했는지

        q.offer(n);
        visited[n] = 1;

        while(!q.isEmpty()) {
            int x = q.poll();

            if (x == k) break;

            for (int next : new int[]{x-1, x+1, x*2}){
                if (next >= 0 && next < MAX && visited[next] == 0) {
                    q.offer(next); // 6
                    visited[next] = visited[x] + 1; // visited[6] = visited[5] + 1 = 2
                    parent[next] = parent[x] + 1; // parent[6] = parent[5]  + 1
                }
            }
        }

        System.out.println(visited[k] - 1);


        List<Integer> path = new ArrayList<>();
        int temp = k;
        while (temp != n) {
            path.add(temp);
            temp = parent[temp];
        }
        path.add(n);

        Collections.reverse(path);

        for (int p : path) System.out.println(p + " ");
    }
}
