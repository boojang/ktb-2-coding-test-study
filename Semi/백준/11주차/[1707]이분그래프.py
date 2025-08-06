'''
Author    : semi
Date      : 2025.07.23(Wed)
Runtime   : 1704ms
Memory    : 53244KB
Algorithm : BFS
'''

import sys
from collections import deque

input = sys.stdin.readline

K = int(input())

for _ in range(K):
    ans = 'YES'
    
    V, E = map(int, input().split()) # 정점갯수 , 간선 갯수

    #중복 간선 제외 -> set 사용
    graph = [set() for _ in range(V+1)]
    binary_group = [0] * (V+1) #0:그룹미지정 /1:그룹1 /2:그룹2

    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].add(v)
        graph[v].add(u)
        
    for i in range(1,V+1):
        
        if binary_group[i] == 0:
            queue = deque() # 큐 생성
            queue.append(i)
            binary_group[i] = 1 # 그룹1로 설정

            while queue:  # 이분그래프 확인 -> BFS로 탐색

                ve = queue.popleft()

                for j in graph[ve]:

                    if binary_group[j] == 0:
                        num = 2 if binary_group[ve] == 1 else 1
                        binary_group[j] = num
                        queue.append(j)
                    else:
                        if binary_group[ve] == binary_group[j]:
                            # print(f"ve:{ve},j:{j}, binary_group[ve]:{binary_group[ve]}, binary_group[j]:{binary_group[j]}")
                            ans = 'NO'


    print(ans)


