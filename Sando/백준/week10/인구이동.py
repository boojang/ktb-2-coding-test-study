# * https://www.acmicpc.net/problem/16234
# * Author : Kang San Ah
# * Date : 2025.07.15(Mon)
# * Runtime : 2 sec
# * Memory : 512 MB
# * Algorithm : BFS

from collections import deque 
import sys
import math

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n,l,r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)] # 2차원 배열

def BFS(x,y,visited):
    q = deque()
    q.append((x,y))
    union = [(x,y)]
    sum = 0
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx  < n and  0 <= ny < n and not visited[nx][ny]:
                if l <= abs(arr[x][y]-arr[nx][ny]) <= r: # l,r 범위 내인지 확인
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    union.append((nx,ny))
                    sum += arr[cx][cy] # 총합 더하기
    
    # 인구 분배             
    if len(union) > 1:
        avg = sum // len(union)
        for ux,uy in union : 
            arr[ux][uy] = avg
        return True
    
    return False
    
days = 0
while True:
    move = False
    visited = [[False] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if BFS(i,j,visited):
                    move = True
    if not move:
        break
    days+=1

print(days)                    