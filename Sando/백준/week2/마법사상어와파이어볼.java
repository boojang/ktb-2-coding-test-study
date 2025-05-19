package 백준.week2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * Author    : Kang San Ah
 * Date      : 2025.04.16(Wed)
 * Runtime   : 2 sec
 * Memory    : 128 MB
 * Algorithm : Simulation
 */

class Fireball{
    int r;
    int c;
    int m;
    int s;
    int d;

    public Fireball(int r, int c, int m, int s, int d) {
        this.r = r;
        this.c = c;
        this.m = m; // 질량
        this.s = s; // 속도
        this.d = d; // 방향
    }
}

// https://www.acmicpc.net/problem/20056
public class 마법사상어와파이어볼 {

    static StringTokenizer st;
    static int N,M,K;

    static int[] dr = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dc = {0, 1, 1, 1, 0, -1, -1, -1};

    static int [][] arr;

    public static int simulation (int N, int K, List<Fireball> f){
        int answer = 0 ;
        List<Fireball>[][] map = new ArrayList[N][N];
        for (int i = 0 ; i < N; i ++){
            for (int j = 0 ; j < N; j ++){
                map[i][j] = new ArrayList<>();
            }
        }

        while (K --> 0){
            List<Fireball> next = new ArrayList<>();
            // 이동
            for (Fireball fireball : f) {
                // modulo 연산
                int nr = (fireball.r + dr[fireball.d] * fireball.s ) % N;
                int nc = (fireball.c + dc[fireball.d] * fireball.s ) % N;
                map[nr][nc].add(new Fireball(nr, nc, fireball.m, fireball.s, fireball.d));
            }


            for (int i = 0 ; i < N ; i ++){
                for (int j = 0 ; j < N ; j++){
                    // 1개 파이어 볼이 있는 칸에서 일어나는 동작
                    if (map[i][j].size() == 1){
                        next.add(map[i][j].get(0));
                    }
                    // 2개 이상의 파이어 볼이 있는 칸에서 일어나는 동작
                    if (map[i][j].size() >=2) {

                        int mTotal = 0;
                        int sTotal = 0;
                        boolean allEven = true;
                        boolean allOdd = true;
                        for (Fireball x : map[i][j]){
                            mTotal += x.m;
                            sTotal += x.s;
                            if (x.d % 2 ==0) allOdd = false;
                            else allEven = false;
                        }

                        int [] nd;
                        if (allEven || allOdd) nd = new int[]{0,2,4,6};
                        else nd = new int[]{1, 3, 5, 7};

                        // 병합 결과 덮어쓰기
                        int newM = mTotal / 5 ;
                        if (newM > 0) {
                            int newS = sTotal / map[i][j].size();
                            for (int d : nd){
                                next.add(new Fireball(i, j, newM, newS, d));
                            }
                        }
                    }
                }
            }
            // map 초기화
            for (int i = 0; i < N ; i++){
                for (int j = 0 ; j < N ; j++){
                    map[i][j].clear();
                }
            }
            f = next;
        }

        // 총 질량 구하기
        for (Fireball x : f) answer += x.m;
        return answer;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        arr = new int [N][N];
        List<Fireball> f = new ArrayList<>();

        for (int i = 0 ; i < M; i ++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            f.add(new Fireball(r-1,c-1,m,s,d));
        }

        System.out.println(simulation(N,K,f));

    }


}
