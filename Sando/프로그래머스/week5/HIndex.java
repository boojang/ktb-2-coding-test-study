package 프로그래머스.week5;

import java.util.*;

/**
 * Author    : Kang San Ah
 * Date      : 2025.05.23(Fri)
 * Algorithm : Sort
 */

public class HIndex {

    // 1번째 방법
    public int solution(int[] citations) {
        int answer = 0;
        Integer[] boxed = Arrays.stream(citations).boxed().toArray(Integer[]::new);
        Arrays.sort(boxed,Collections.reverseOrder());
        for (int i = 1 ; i <= boxed.length; i ++) {
            if (i <= boxed[i-1]) answer++;
            else return answer;
        }
        return answer;
    }

    // 2번째 방법
    public int solution2(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);// 오름차순 정렬 [0,1,3,5,6] 61 52 53 44
        for (int i = citations.length-1 ; i >= 0; i --) {
            if (citations.length-i > citations[i]) return citations.length - i - 1;
        };
        return citations.length;
    }

}
