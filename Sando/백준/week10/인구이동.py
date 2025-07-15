from collections import deque
import sys
input = sys.stdin.readline

# 방향 벡터 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 입력
n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    union = [(x, y)]  # 연합에 포함된 좌표들
    total = arr[x][y]

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(arr[cx][cy] - arr[nx][ny]) <= r:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    union.append((nx, ny)) # [(0,0) , (1,1)...]
                    total += arr[nx][ny]

    # 연합을 형성했다면 평균으로 인구 분배
    if len(union) > 1:
        avg = total // len(union)
        for ux, uy in union:
            arr[ux][uy] = avg
        return True  # 인구 이동 발생

    return False  # 인구 이동 없음

# 메인 로직
days = 0
while True:
    visited = [[False] * n for _ in range(n)]
    moved = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    moved = True

    if not moved:
        break
    days += 1

print(days)
