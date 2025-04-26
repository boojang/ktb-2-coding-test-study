package 백준.week3;





import java.util.*;
import java.io.*;


class Main {


    static class Point{
        int x;
        int y;

        Point(int x, int y){
            this.x = x;
            this.y = y;
        }
    }

    static StringTokenizer st;
    static int[] dy = {0, 1, 1, 1, 0, -1,-1,-1};
    static int[] dx = {-1, -1, 0 , 1, 1, 1, 0, -1};
    static int N, M, answer;
    static int[][]arr;

    public static int bfs(int x, int y) {
        boolean[][] visited = new boolean[N][M];
        Queue<Point> q = new LinkedList<>();
        q.offer(new Point(x, y));
        visited[x][y] = true;

        int distance = 0;

        while (!q.isEmpty()) {
            int size = q.size(); // 현재 거리 level의 노드 개수
            distance++;

            for (int s = 0; s < size; s++) {
                Point p = q.poll();

                for (int i = 0; i < 8; i++) {
                    int nx = p.x + dx[i];
                    int ny = p.y + dy[i];

                    if (nx >= 0 && nx < N && ny >= 0 && ny < M && !visited[nx][ny]) {
                        if (arr[nx][ny] == 1) {
                            return distance;
                        }
                        visited[nx][ny] = true;
                        q.offer(new Point(nx, ny));
                    }
                }
            }
        }

        return 0;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N][M];


        for(int i = 0 ; i < N ; i ++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0 ; j < M ; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        answer = Integer.MIN_VALUE;

        for(int i = 0 ; i < N ; i ++){
            for(int j = 0 ; j < M; j++) {
                if(arr[i][j] == 0){
                    answer = Math.max(answer, bfs(i,j));
                }
            }
        }

        System.out.println(answer);
    }
}

