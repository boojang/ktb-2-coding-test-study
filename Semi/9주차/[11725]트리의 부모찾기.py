'''
Author    : semi
Date      : 2025.07.09(Wed)
Runtime   : 2564ms
Memory    : 52508KB
Algorithm : BFS
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

#인접 리스트 -> 연결되어있는 노드를 저장
graph = [[] for _ in range(n+1)]


for i in range(n-1):
    a , b = map(int,input().split())
    #연결되어 있는 것들이 다 들어가있음 -> 누가 부모인지 자식인지 모름
    graph[a].append(b)
    graph[b].append(a)
print(graph)

# BFS 탐색용 큐 -> 루트노드 1부터 시작
queue = deque([1])
#부모노드 기록
parent = [0] * (n+1)

while queue:
    # queue에서 노드를 빼낸다. 연결되어 있는 다음 노드로 이동
    current = queue.popleft()
    for node in graph[current]:
        if parent[node] == 0 : #아직 부모가 없다 -> 방문 하지 않았다.
            parent[node] = current
            queue.append(node) #다음에 방문할 노드로 추가한다.

for p in parent[2:]:
    print(p)