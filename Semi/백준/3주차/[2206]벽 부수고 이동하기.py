# N*M 행렬
# 최단 경로로 이동
# 맴에서 가장 적은 개수의 칸을 지나는 경로
# 1,1 -> n,m의 위치까지 이동
# 만약 이동 도중 한개의 벽을 부수면 짧아진다 -> ㅕㄱ 한개를 부수고 이동해도 된다.
from collections import deque;

maps = []
direction=[(-1,0),(1,0),(0,-1),(0,1)]
distance =0

# a = map()
# n : row / m : column
n,m = map(int,input().split())

visited = [[0]*m for _ in range(n)]

# 0 : 이동할 수 있는 곳 / 1: 이동할 수 없는 벽
for i in range(n):
    # 입력 받은 한줄을 1차 리스트로 바꿔야한다.
    a = list(map(int,input()))
    maps.append(a)


#print(maps)
#print(len(maps)) # 열의 갯수
#print(len(maps[0])) # 행의 갯수

# (0,0) -> (n-1,m-1) 까지 최단 거리
# 0일때만 갈 수 있다. -> maps[i][j] == 0
# 그럼 '탐색'을 해야한다.
# x,y

def bfs(sr,sc):
    queue = deque()
    queue.append((sr,sc))

    while queue:
        r,c = queue.popleft()

        for dr,dc in direction:
            nr,nc = r+dr,c+dc

    return distance

# 시작점에서 시작해서 도착점까지 한 번만 탐색해야한다.
for i in range(n):
    for j in range(m):
        current_max = bfs()
        distance = max(current_max,distance)

