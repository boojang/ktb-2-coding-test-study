# https://www.acmicpc.net/problem/13460

# * Author : Kang San Ah
# * Date : 2025.07.22(Tue)
# * Runtime : 2 sec
# * Memory : 512 MB
# * Algorithm : BFS

# 고려 사항
# 1. 동시에 빠지면 안됨 -> 즉 같은 방향에서 출발해서 구멍에 들어가면 x
# 2. 기울인다 -> R과B가 현재 위치에서 같은 방향으로 움직인다.
# 3. R 기준으로 움직일 때 B 상태 추적도 해야 한다.

import sys
input = sys.stdin.readline

from collections import deque

# 이 함수는 일반적인 네 방향으로 뻗치는 BFS가 아닌 한 방향으로 쭈욱 나가는 함수
def move(x,y,dx,dy):
    dist = 0
    while a[x + dx][y + dy] != '#':
        x += dx
        y += dy
        dist += 1
        if a[x][y] == 'O':
            break
    return x,y, dist


n, m = map(int, input().split())

a = list(list(input().strip())for _ in range(n)) # list()는 요소를 하나 씩 쪼개줌.
# [list(map(str, input().strip())) for _ in range(n)] -> ok
# list(list(input().strip())for _ in range(n))        -> ok
# list([input().strip()]for _ in range(n))            -> x, 이건 "#####.#" 등과 같이 한줄로 됨
dx = [-1, 0 , 1, 0]
dy = [0, 1, 0, -1]

visited = [[[[False for j in range(m)]for i in range(n)]for k in range(m)]for h in range(n)]

# Red, Blue 위치 찾기
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == 'R':
            rx, ry = i, j
        elif a[i][j] == 'B':
            bx, by = i, j
        
# BFS 시작
q = deque()
visited[rx][ry][bx][by] = True

q.append((rx,ry,bx,by,0))

while q:
    crx, cry, cbx, cby, depth = q.popleft()
    
    if depth >= 10 :
        break
    
    for i in range(4):
        nrx,nry,r_dist = move(crx,cry,dx[i],dy[i]) # 이 함수를 통해 빨간구슬이 벽 혹은 구멍을 마추칠때까지 이동한 좌표와 거리 값이 나온다.
        nbx,nby,b_dist = move(cbx,cby,dx[i],dy[i]) # 이 함수를 통해 파란구슬이 벽 혹은 구멍을 마추칠때까지 이동한 좌표와 거리 값이 나온다.
        
        # 파란 구슬이 빠졌는지 확인
        if a[nbx][nby] == 'O':
            continue # 실패 처리 
    
        # 빨간 구슬이 구멍에 빠지고, 파란 구슬이 빠지지 않았다면 성공
        if a[nrx][nry] == 'O':
            print(depth + 1)
            sys.exit(0) # 시스템 종료
        
        # 두 구슬이 같은 벽에 막혔다면, 이동 거리가 더 먼 구슬을 한칸 뒤로 민다.
        if nrx == nbx and nry == nby :
            if r_dist > b_dist :
                nrx -= dx[i]
                nry -= dy[i]
            else :
                nbx -= dx[i]
                nby -= dy[i]                 
        
        if not visited[nrx][nry][nbx][nby] :
            visited[nrx][nry][nbx][nby] = True
            q.append((nrx,nry,nbx,nby, depth + 1))
    
print(-1)

