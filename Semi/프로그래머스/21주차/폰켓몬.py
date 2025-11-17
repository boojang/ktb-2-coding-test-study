'''
https://school.programmers.co.kr/learn/courses/30/lessons/1845
Author    : semi
Date      : 2025.10.03(Fri)
Algorithm :
'''
# n/2마리 고를 수 있다.
# 가장 많은 "종류"의 폰켓몬 선택

from collections import Counter

def solution(phoneketmon):
    leng = len(phoneketmon) // 2
    phoneketmon = Counter(phoneketmon)

    answer = min(len(phoneketmon) , leng)

    return answer


solution([3,3,3,2,2,4])