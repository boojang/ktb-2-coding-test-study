'''
Author    : semi
Date      : 2025.08.05(Tues)
Runtime   : ms
Memory    : KB
Algorithm : BFS
'''

from collections import deque

def solution(x, y, n):
    queue = deque()
    queue.append((x, 0))
    visited = set()
    visited.add(x)
    
    #BFS
    while queue:
        now, cnt = queue.popleft()
        if now == y:
            return cnt
        # 다음에 방문할 수 있는 경우
        for next in [now + n, now * 2, now * 3]:
            # 범위 체크 & 방문 여부 확인
            if next <= y and next not in visited:
                visited.add(next)
                queue.append((next, cnt + 1))
    return -1