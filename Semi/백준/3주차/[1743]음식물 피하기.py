'''
Author    : semi
Date      : 2025.04.24(Thr)
Runtime   : 184ms
Memory    : 36016KB
Algorithm :
'''

n,m,k = map(int,input().split())
board = [[0]*m for _ in range(n)] 
visited = [[False]*m for _ in range(n)] 

directions = [(-1,0),(1,0),(0,-1),(0,1)]
max_size =0

for i in range(k):
    r,c=map(int,input().split())
    board[r-1][c-1]=1 #음식물
    

from collections import deque

def bfs(sr,sc):
    queue = deque()
    queue.append((sr,sc))
    visited[sr][sc] = True
    count =1

    while queue:
        
        r,c = queue.popleft()

        for dr,dc in directions:
            nr , nc = r +dr, c +dc
            
            # outbound
            if 0 <= nr < n and 0 <= nc < m :
                if board[nr][nc] == 1 and not visited[nr][nc]:
                    # print(f"→ 탐색: ({nr}, {nc})")
                    visited[nr][nc] = True
                    queue.append((nr,nc))
                    count +=1

    return count

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            size=bfs(i,j)
            max_size = max(max_size,size)

print(max_size)