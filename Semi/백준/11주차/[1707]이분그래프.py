'''
Author    : semi
Date      : 2025.07.23(Wed)
Runtime   :
Memory    :
Algorithm : BFS
'''

from collections import deque

K = int(input())

for _ in range(K):
    queue = deque([])
    ans = 'YES'
    # 정점갯수 , 간선 갯수
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    binary_group = [0] * (V+1) #0:그룹미지정 /1:그룹1 /2:그룹2
    binary_group[1] = 1 #미리 설정

    for _ in range(E):
        # 인접한 정점 번호
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)


    # 이분그래프 확인 -> BFS로 탐색
    while queue:

        ve = queue.popleft()

        for i in graph[ve]:
            # 인접한 애들을 델고와
            # 인접한 애들은 나랑 다른 그룹이여야해
            # 누구를 queue에 넣을까? 인접한 애들을 넣자

            if binary_group[i] == 0:
                num = 2 if binary_group[ve] ==1 else 1
                binary_group[i] = num
                #ve랑은 다른 그룹으로 설정
                #만약 ve랑 같은 그룹이면 ans는 no
                queue.append(i)
            else:

                if binary_group[ve] == binary_group[i]:
                    print('진입')
                    ans = 'NO'


    print(ans)


