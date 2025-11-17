'''
https://school.programmers.co.kr/learn/courses/30/lessons/84512
Author    : semi
Date      : 2025.09.25(Thurs)
Algorithm : stack/queue
'''
from collections import deque

def solution(priorities, location):
    queue = deque(list(enumerate(priorities)))
    answer = 0
    while queue:
        c_p = queue.popleft()
        # queue에 남아있는 item 중 c_p보다 높은 item이 하나라도 있는지
        if any(c_p[1] < item[1] for item in queue):
            queue.append(c_p)
            continue
        else:
            answer += 1
            if location == c_p[0]:
                return answer





solution([1, 1, 9, 1, 1, 1],0)