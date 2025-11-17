'''
Author    : semi
Date      : 2025.11.03(Mon)
Runtime   : 68
ms
Memory    : 34968KB
Algorithm :
'''

'''
test case T
가로길이 m
세로길이 n
배추가 심어져 있는 위치 갯수 k

- 지렁이 -> 서로 인접해 있으며 이동가능
- 필요한 최소 배추흰지렁이 마리 수
- 목표 : 서로 인접해 있는 배추 집합의 갯수를 구해라.
- ex) 그림에는 총 5개의 배추 집합이 있다.
'''

'''
어떻게 인접한지 알까? 탐색해야한다. 만약 상하좌우에 포함한다. -> 그럼 탐색 큐로 사용한다.
'''

import sys
from collections import deque

input = sys.stdin.readline

direction = [(1,0),(-1,0),(0,1),(0,-1)]


def bfs(cabage):
    visited= set() #방문한 좌표
    area = 0
    
    #모든 좌표 방문
    for start in cabage:
        if start in visited: #방문 했으면 다른 좌표
            continue

        area +=1 #새로운 군집 시작
        queue = deque([start])
        visited.add(start)

        while queue:
            x, y = queue.popleft()
            # 상하좌우로 움직인다.
            for dx, dy in direction:
                nx, ny = x + dx, y + dy  # 새로운 좌표
                if (nx, ny) in cabage and (nx, ny) not in visited:
                    queue.append((nx, ny))  # 탐색할 좌표로 추가
                    visited.add((nx, ny))  # 방문한 좌표로 추가


    return area


T = int(input())

for _ in range(T):
    M,N,K = map(int,input().split())

    cabage = set()
    for _ in range(K):
        x,y = map(int,input().split())
        cabage.add((x,y))

    answer = bfs(cabage)
    print(answer)
