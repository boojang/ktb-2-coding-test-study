package 백준.week2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * Author    : Kang San Ah
 * Date      : 2025.04.18(Fri)
 * Runtime   : 1 sec
 * Memory    : 512 MB
 * Algorithm : Simulation
 */

// https://www.acmicpc.net/problem/20057
public class 마법사상어와토네이도 {

    static int [][] arr;
    static List<Integer[]> move = new ArrayList<>();
    static StringTokenizer st;
    static int N;

    static int[] dr = {0, 1, 0, -1};
    static int[] dc = {-1, 0, 1, 0};

    public static void simulation(){

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        arr = new int[N][N];

        for (int i = 0 ; i < N ; i ++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0 ; j < N; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int r = N / 2;
        int c = N / 2;

        int dir = 0;

        // 좌측 상단 0,0이 되기 전까지 방향 저장
//        while (!(r == 0) &&  (c == 0)) {
//            for (int i )
//        }
    }
}
