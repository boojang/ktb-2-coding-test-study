'''
Author    : semi
Date      : 2025.04.24(Thr)
Runtime   : 184ms
Memory    : 36016KB
Algorithm :
'''

# 통로 세로 길이 n [1,100] ,가로 길이 m [1,100]
# 음식물 쓰레기 개수 k [1,n*m]
# k개 만큼 r,c 
# 가장 큰 음식물의 크기 
# 근처에 있는 것끼리 뭉친다. -> 상하좌우를 봐야한다.

n,m,k = map(int,input().split())
board = [[0]*m for _ in range(n)] #음식물 격자
visited = [[False]*m for _ in range(n)] #방문여부 격자 -> 5...
# 1,0 -> int -> 4byte
# true,false -> 1byte

#방향 벡터
directions = [(-1,0),(1,0),(0,-1),(0,1)]
max_size =0

for i in range(k):
    r,c=map(int,input().split())
    board[r-1][c-1]=1 #음식물
    
    
# 1) 각 요소 -> 상하좌우에 연속된 쓰레기가 있는가.

# 현재 크기 n * m -> 상하좌우 연결 여부 체크 
# -> 전체 통로를 어떻게 알까?
# -> 좌표 하나에서 출발해 연결된 음식을 어떻게 찾을까

 
# 2) 연속된 쓰레기 값을 어떻게 count 할것인가?

# 상하좌우로 인접한 것을 하나로 묶는 문제 -> 대표적인 그래프 탐색 문제

# 전체 격자 위에 음식물이 있는 위치를 표시하고,
# 그걸 바탕으로 탐색하며 개수 세는 방식

# BFS
# 왜 BFS 시 deque를 사용했는가?
# java -> 그냥 queue를 사용한다.
# 
from collections import deque

def bfs(sr,sc):
    queue = deque()
    queue.append((sr,sc))
    visited[sr][sc] = True
    count =1

    # print(f"[START] bfs 시작점: ({sr}, {sc})")

    while queue:
        # 
        r,c = queue.popleft() #제일 앞 요소가 삭제

        # print(f"→ 탐색 중: ({r}, {c})")

        # 방향대로
        for dr,dc in directions:
            nr , nc = r +dr, c +dc
            # print(f"→ 탐색 하는 위치: ({nr}, {nc})")

            # outbound
            if 0 <= nr < n and 0 <= nc < m :
                if board[nr][nc] == 1 and not visited[nr][nc]:
                    # print(f"→ 탐색: ({nr}, {nc})")
                    visited[nr][nc] = True
                    queue.append((nr,nc))
                    count +=1
                    # print(f"  ↳ 연결된 음식물 발견: ({nr}, {nc}), 현재 크기: {count}")

        # print(f"[END] 음식물 덩어리 크기: {count}")

    return count



# 쓰레기가 있고 + 방문하지 않았다면
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            size=bfs(i,j)
            max_size = max(max_size,size)

print(max_size)