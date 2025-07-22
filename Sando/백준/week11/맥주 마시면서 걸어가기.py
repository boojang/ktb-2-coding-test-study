# https://www.acmicpc.net/problem/9205

# * Author : Kang San Ah
# * Date : 2025.07.22(Tue)
# * Runtime : 1 sec
# * Memory : 128 MB
# * Algorithm : BFS

import sys
input = sys.stdin.readline

from collections import deque

def can_go(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) <= 1000

def BFS():
    q = deque()
    q.append(start)
    visited = [False] * len(points)

    while q:
        x, y = q.popleft()
        if (x, y) == end:
            return True
        for i in range(len(points)):
            if not visited[i] and can_go((x, y), points[i]):
                visited[i] = True
                q.append(points[i])
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    start = tuple(map(int, input().split()))
    points = [tuple(map(int, input().split())) for _ in range(n)]
    end = tuple(map(int, input().split()))
    points.append(end)

    print("happy" if BFS() else "sad")
