'''
https://school.programmers.co.kr/learn/courses/30/lessons/84512
Author    : semi
Date      : 2025.09.25(Thurs)
Algorithm :
'''
from collections import deque

def solution(priorities, location):
    pri_list = list(enumerate(priorities))
    pri_max = max(priorities)
    answer = 0
    while len(pri_list)!=0:
        c_p = pri_list.pop(0)
        if(c_p[1]<pri_max):
            pri_list.append(c_p)
            continue

        answer +=1

        if any(pri_list):
            pri_max = max(x[1] for x in pri_list)

        if location == c_p[0]:
            return answer



solution([1, 1, 9, 1, 1, 1],0)