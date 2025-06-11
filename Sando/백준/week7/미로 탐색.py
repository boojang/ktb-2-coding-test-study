#  * Author    : Kang San Ah
#  * Date      : 2025.06.11(Wed)
#  * Runtime   : 1 sec
#  * Memory    : 192 MB
#  * Algorithm : BFS

from collections import deque
import sys 
input = sys.stdin.readline

n,m = map(int,input().split())

a = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x,y):
    dq = deque()
    dq.append((x,y))
    while dq:
        x,y = dq.popleft()
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >=0 and ny < m  and a[nx][ny] == 1:
                a[nx][ny] = a[x][y] + 1
                dq.append((nx,ny))

BFS(0,0)
print(a[n-1][m-1])
    