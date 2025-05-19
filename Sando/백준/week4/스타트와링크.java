package 백준.week4;

import java.io.*;
import java.util.*;

/**
 * Author    : Kang San Ah
 * Date      : 2025.05.18(Sun)
 * Runtime   : 2 sec
 * Memory    : 512 MB
 * Algorithm : DFS
 */

public class 스타트와링크 {

    static int N;
    static StringTokenizer st;
    static int[][] S;
    static boolean [] team ;
    static int answer = Integer.MAX_VALUE;
    static void dfs(int depth, int start){
        if (depth == N / 2) {
              calc();
              return;
        }else{
            for (int i = start ; i < N; i++){
                team[i] = true;
                dfs(depth + 1 , i + 1);
                team[i] = false;
            }
        }
    }

    static void calc(){
        int startTeam = 0 ; int linkTeam = 0;
        for (int i = 0 ; i < N; i++){
            for (int j = i + 1 ; j < N; j++){
                if (team[i] && team[j]){
                    startTeam += S[i][j] + S[j][i];
                }else if(!team[i] && !team[j]){
                    linkTeam += S[i][j] + S[j][i];
                }
            }
        }
        int diff = Math.abs(startTeam - linkTeam);
        answer = Math.min(answer, diff);
        if (answer == 0){
            System.out.println(answer);
            System.exit(0); // 종료
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        S = new int[N][N];
        team = new boolean[N];

        for (int i = 0 ; i < N ; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0 ; j < N ; j++){
                S[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dfs(0,0);
        System.out.println(answer);
    }


}
