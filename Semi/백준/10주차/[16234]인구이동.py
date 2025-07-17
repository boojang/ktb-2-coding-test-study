'''
Author    : semi
Date      : 2025.07.16(Wed)
Runtime   : ms
Memory    : KB
Algorithm : 
'''

from collections import deque

N, L, R = map(int, input().split())

A = []

for i in range(N):
    A.append(list(map(int, input().split())))

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, visited):
    q = deque()
    q.append((r, c))
    union = [(r, c)]
    visited[r][c] = True
    total_pop = A[r][c]

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dr[d]
            ny = y + dc[d]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                diff = abs(A[x][y] - A[nx][ny])
                if L <= diff <= R:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    union.append((nx, ny))
                    total_pop += A[nx][ny]

    # 연합 인구 이동
    if len(union) > 1:
        new_pop = total_pop // len(union)
        for x, y in union:
            A[x][y] = new_pop
        return True
    return False

# 전체 반복
days = 0
while True:
    visited = [[False]*N for _ in range(N)]
    moved = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    moved = True

    if not moved:
        break
    days += 1

print(days)
