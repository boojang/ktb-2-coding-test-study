package 백준.week6;

import java.io.*;
import java.util.*;

public class 오리 {
    static final String QUACK = "quack";

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] input = br.readLine().toCharArray();

        List<Integer> ducks = new ArrayList<>();
        int maxDucks = 0;

        for (char ch : input) {
            int idx = QUACK.indexOf(ch);

            boolean assigned = false;

            for (int i = 0; i < ducks.size(); i++) {
                if (ducks.get(i) == idx - 1) {
                    ducks.set(i, idx);
                    assigned = true;
                    break;
                }
            }

            if (idx == 0 && !assigned) {
                ducks.add(0);
                assigned = true;
            }

            if (!assigned) {

                System.out.println(-1);
                return;
            }

            ducks.removeIf(state -> state == 4);

            maxDucks = Math.max(maxDucks, ducks.size());
        }

        if (!ducks.isEmpty()) {
            System.out.println(-1);
        } else {
            System.out.println(maxDucks);
        }
    }
}

