package 백준.week3;

import java.util.*;
import java.io.*;

/**
 * Author    : Kang San Ah
 * Date      : 2025.04.27(Sun)
 * Runtime   : 2 sec
 * Memory    : 128 MB
 * Algorithm : BFS
 */

// https://www.acmicpc.net/problem/1743
class 음식물피하기 {

    static class Point {
        int x;
        int y;

        Point(int x, int y){
            this.x = x;
            this.y = y;
        }
    }

    static StringTokenizer st;

    static int N, M, K ;

    static int [][] arr;
    static int [] dx = {0,1,0,-1};
    static int [] dy = {1,0,-1,0};
    static boolean[][] visited;

    public static int bfs(int x, int y){
        Queue<Point> q = new LinkedList<>();
        q.offer(new Point(x,y));
        visited[x][y] = true;
        int cnt = 1 ;
        while(!q.isEmpty()){
            Point p = q.poll();
            for(int i = 0 ; i < 4 ; i ++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];

                if(nx >= 0 && nx < N && ny >= 0 && ny < M && visited[nx][ny] == false && arr[nx][ny] == 1) {
                    cnt ++;
                    visited[nx][ny] = true;
                    q.offer(new Point(nx,ny));
                }
            }
        }
        return cnt;
    }

    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        arr = new int[N][M];
        visited = new boolean[N][M];

        for(int i = 0 ; i  < K ; i ++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken()) - 1;
            int y = Integer.parseInt(st.nextToken()) - 1;
            arr[x][y] = 1;
        }

        int answer = 0;
        for(int i = 0 ; i < N ; i ++) {
            for(int j = 0 ; j < M ; j++) {
                if(arr[i][j] == 1) {
                    answer = Math.max(answer, bfs(i,j));
                }
            }
        }
        System.out.println(answer);
    }
}