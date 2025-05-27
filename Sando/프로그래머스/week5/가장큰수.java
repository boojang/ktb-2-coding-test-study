package 프로그래머스.week5;

import java.util.*;

/**
 * Author    : Kang San Ah
 * Date      : 2025.05.22(Thu)
 * Algorithm : Sort
 */

class 가장큰수 {
    public String solution(int[] numbers) {

        StringBuilder sb = new StringBuilder();
        String[] arr = new String[numbers.length];

        for(int i = 0 ; i< arr.length; i++){
            arr[i] = String.valueOf(numbers[i]);
        }

        Arrays.sort(arr, (o1,o2) -> (o2+o1).compareTo(o1+o2));

        if(arr[0].equals("0")) return "0";

        for(String num : arr) {
            sb.append(num);
        }

        return sb.toString();
    }
}
