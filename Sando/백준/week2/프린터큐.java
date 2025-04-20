package 백준.week2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * Author    : Kang San Ah
 * Date      : 2025.04.14(Mon)
 * Runtime   : 2 sec
 * Memory    : 128 MB
 * Algorithm : Simulation, Priority Queue
 */

class Docs implements Comparable<Docs>{
    int idx;
    int priority;
    Docs(int idx, int priority){
        this.idx = idx;
        this.priority = priority;
    }

    @Override
    public int compareTo(Docs o) {
        return o.priority - this.priority;
    }
}

//https://www.acmicpc.net/problem/1966
public class 프린터큐 {

    public static StringBuilder sb = new StringBuilder();
    static int a,b;
    public static StringTokenizer st;

    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());

            Queue<Docs> q = new LinkedList<>();
            PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < a; j++) {
                int priority = Integer.parseInt(st.nextToken());
                q.add(new Docs(j, priority));
                pq.add(priority);
            }

            int cnt = 0;
            while (!q.isEmpty()) {
                Docs current = q.poll();
                if (current.priority == pq.peek()) {
                    cnt++;
                    pq.poll();
                    if (current.idx == b) {
                        sb.append(cnt).append("\n");
                        break;
                    }
                } else {
                    q.add(current);
                }
            }
        }
        System.out.println(sb);
    }
}
