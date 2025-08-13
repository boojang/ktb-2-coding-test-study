# https://school.programmers.co.kr/learn/courses/30/lessons/150365

# * Author : Kang San Ah
# * Date : 2025.08.13(Wed)
# * Algorithm : BFS

def solution(n, m, x, y, r, c, k):
    from heapq import heappush, heappop

    directions = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]
    
    tx, ty = r - 1, c - 1
    hq = []
    heappush(hq, ("", x - 1, y - 1, 0))  

    while hq:
        path, cx, cy, dist = heappop(hq)

        if dist == k:
            if (cx, cy) == (tx, ty):
                return path
            continue 

        remain = k - dist
        min_dist = abs(cx - tx) + abs(cy - ty)

        if min_dist > remain or (remain - min_dist) % 2 != 0:
            continue  

        for ch, dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m:
                heappush(hq, (path + ch, nx, ny, dist + 1))

    return "impossible"



# 시간 초과
# def solution(n, m, x, y, r, c, k):
#     answer = ''
#     from collections import deque
    
#     # k가 개수
#     # d,l,r,u 순으로 정렬
#     dir = [('d' , 1, 0) , ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]
    
#     q = deque()
#     q.append((x-1,y-1 , 0, ""))
#     tx, ty = r-1, c-1
    
#     while q : 
#         cx, cy, dist, path = q.popleft()
#         if dist == k and (cx, cy) == (tx, ty) :
#             return path
        
#         # 불필요한 좌표 걸러내기
#         remain_dist = k - dist
#         min_dist = abs(cx - tx) + abs(cy - ty)
#         if min_dist > remain_dist or (remain_dist - min_dist) % 2 != 0:
#             continue # 홀수면 안됨.
        
#         for ch, dx, dy in dir : 
#             nx, ny = cx + dx, cy + dy
#             if 0 <= nx < n and 0 <= ny < m : 
#                 q.append((nx,ny, dist+1, path+ch))
            
    
#     return "impossible"