# https://www.acmicpc.net/problem/1389

# * Author : Kang San Ah
# * Date : 2025.07.21(Mon)
# * Runtime : 2 sec
# * Memory : 128 MB
# * Algorithm : 

import sys
from collections import deque
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)


# def DFS(node) : 
#     visited[node] = True
#     for i in a[node]:
#         if not visited[i]:
#             DFS(i)
            
#     return sum            


def BFS(node) :
    sum = 0 
    q = deque()
    visited[node] = True
    q.append((node,0))
    while q:
        c, s = q.popleft()
        for i in a[c]:
            if not visited[i]:
                visited[i] = True
                q.append((i,s+1))
                if arr[i] == 0:
                    arr[i] = s+1
    for i in arr:
        sum += i if i != 0 else 0
    return sum
           
                     
n,m = map(int, input().split())
a = [[] for _ in range(n+1)] # v개의 인접 리스트 생성


# 인접 리스트 연결
for _ in range(m):
    v,e = map(int, input().split())
    a[v].append(e)
    a[e].append(v)

li = [0] * (n+1)
for i in range(1, n+1):
    arr = [0] * (n+1) 
    visited = [False] * (n+1)
    li[i]=BFS(i)

min_v = li[1]
answer = 1
for i in range(2, n+1):
    if li[i] < min_v :
        min_v = li[i]
        answer = i
print (answer)