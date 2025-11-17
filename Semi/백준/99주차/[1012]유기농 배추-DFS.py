'''
Author    : semi
Date      : 2025.11.03(Mon)
Runtime   : 68 ms
Memory    : 34952KB
Algorithm :
'''

import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6) #dfs가 깊이 들어가도 에러 발생x

direction = [(1,0),(-1,0),(0,1),(0,-1)]

# 한번 조건을 만족한걸 만나면 쭉 들어간다.

def dfs(cabage,position,visited):

    if position in visited:
        return

    visited.add(position)

    for dx,dy in direction:
        nx,ny = dx+position[0],dy+position[1]
        # 이웃 + 아직 방문하지 않은 좌표
        if (nx,ny) in cabage and (nx,ny) not in visited:
            dfs(cabage,(nx,ny),visited)


T = int(input())

for _ in range(T):
    M,N,K = map(int,input().split())

    cabage = set()
    for _ in range(K):
        x,y = map(int,input().split())
        cabage.add((x,y))

    visited = set()  # 방문한 좌표
    area = 0 # 군집
    for start in cabage:
        if start not in visited:
            dfs(cabage,start,visited)
            area +=1

    print(area)
