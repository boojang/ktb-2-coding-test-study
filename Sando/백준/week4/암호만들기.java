package 백준.week4;

/**
 * Author    : Kang San Ah
 * Date      : 2025.05.16(Fri)
 * Runtime   : 2 sec
 * Memory    : 128 MB
 * Algorithm : DFS
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 암호만들기 {

    static char[] out, in;
    static int L, C;
    static StringTokenizer st;

    static void dfs(int depth, int start){
        // start 변수(a,c,i,s,t 중 acis 했으면 s 위치가 start 변수 s 다음에 t를 해야 하기에 필요)
        // start 변수로 인해 중복 방지 하는 것이 자동으로 되므로 visited 배열 필요 x
        if (depth == L){
            int jaum = 0 ; int moum = 0;
            for (char c : out){
               if ("aeiou".indexOf(c) >= 0) jaum ++;
               else moum ++;
            }

            if (jaum >=1 && moum >=2){
                for (char c: out) System.out.print(c);
                System.out.println();
                return;
            };
        }else{
            for (int i = start ; i < C ; i++) {
                out[depth] = in[i];
                dfs(depth + 1 , i + 1);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());

        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        in = new char[C];
        out = new char[L];

        for (int i = 0 ; i < C ; i ++) {
            in[i] = st.nextToken().charAt(0);
        }
        Arrays.sort(in);

        dfs(0, 0);
    }
}
