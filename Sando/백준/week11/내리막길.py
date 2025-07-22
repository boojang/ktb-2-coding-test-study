# https://www.acmicpc.net/problem/1520

# * Author : Kang San Ah
# * Date : 2025.07.21(Mon)
# * Runtime : 2 sec
# * Memory : 128 MB
# * Algorithm : DFS + DP

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)] # 경로를 누적할 배열

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1  # 도착지에 도달한 경로는 1개

    if dp[x][y] != -1:
        return dp[x][y]  # 이미 방문한 경우 저장된 값 반환

    dp[x][y] = 0  # 경로 수 초기화
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))


# 추가 :bfs 풀이로는 풀리지 않음. 
# 이유: 
# 1. 중복 경로 추적 불가 (방문 기록)
# 2. 비효율적, 경로 수를 세는 로직에는 약함

# from collections import deque
# import sys
# input = sys.stdin.readline

# n,m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)] # 2차원 배열
# visited = [[False for j in range(m)] for i in range(n)]
# cnt = 0
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def BFS(x,y):
#     q = deque()
#     q.append((x,y))
#     visited[x][y] = True
#     while q:
#         cx, cy = q.popleft()
#         cv = arr[cx][cy] # 현재 값
#         # 도착지면
#         if cx == n-1 and cy == m-1:
#             return True
#         for i in range(4):
#             nx = cx + dx[i]
#             ny = cy + dy[i]
#             if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
#                 if arr[nx][ny] < cv : # 내리막길
#                     q.append((nx,ny))
#                     visited[nx][ny] = True
             
#     return False
# answer = 0
# while BFS(0,0):
#     answer +=1
    
# print(answer)
