import sys
from collections import deque 
input = sys.stdin.readline

N, M = map(int, input().split())

li = [list(map(int, input().strip().split())) for _ in range(N)]

mv =  [(-1,-1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

# 1 상어 위치 탐색
pt = deque()
for i in range(N):
    for j in range(M):
        if li[i][j] == 1:
            pt.append((i, j))

# 2 상어 위치 기준으로 bfs 진행
# 거리는 이전 위치의 값에서 + 1한 값으로 계산
while pt:
    y, x = pt.popleft()
    for dy, dx in mv:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < N and 0 <= nx < M:
            if li[ny][nx] == 0:
                pt.append((ny, nx))
                li[ny][nx] = li[y][x] + 1


result = 0

# 최대 거리 탐색
for i in li:
    result = max(max(i), result)

# 1부터 시작했으니 -1
print(result-1)