package 프로그래머스.week5;

/**
 * Author    : Kang San Ah
 * Date      : 2025.05.27(Tue)
 * Algorithm : Dynamic programming
 */

import java.util.*;

public class 정수삼각형 {
    public int solution(int[][] triangle) {
        int answer = 0;
        for(int i = 1 ; i < triangle.length ; i ++) { // 레벨
            for(int j = 0 ; j < triangle[i].length ; j ++){
                if(j == 0) triangle[i][j] += triangle[i-1][j];
                else if(j == triangle[i].length -1) triangle[i][j] += triangle[i-1][j-1];
                else triangle[i][j] += Math.max(triangle[i-1][j-1] , triangle[i-1][j]);
            }
        }

        for(int i = 0 ; i < triangle[triangle.length-1].length ; i ++) {
            answer = Math.max(answer, triangle[triangle.length-1][i]);
        }

        return answer;
    }
}
