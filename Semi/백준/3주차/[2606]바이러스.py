'''
Author    : semi
Date      : 2025.04.27(Sun)
Runtime   : 184ms
Memory    : 36016KB
Algorithm :
'''

from collections import deque
# 1번 컴퓨터가 바이러스에 걸림 -> 1번을 통해 웜 바이서르에 걸리게 되는 컴퓨터 수

# 컴퓨터의 수 (<=100)
# 연결되어 있는 컴퓨터의 쌍 수
# 연결되어있는 것들

# 연결되어있다 -> 무엇으로 표현? 바로 큐로 저장할까?
# 좌표가 아니라 노드로 연결되어있음


n = int(input())
m = int(input())

# 리스트 형태로 저장 -> 노드 이웃을 바로 꺼낼 수 있다,
# graph[i]로 이웃을 확인할 수 있다. -> index를 노드로 사용하자.
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    # graph[b].append(a)

# 1번에서 출발 -> 1과 묶여있는 애가 있다. -> 그 아이를 큐에 넣는다.
# -> 큐에 들어가고 그 아이로 시작하는 아이를 찾는다.
# 그리고 큐를 뺄때 count를 추가한다?

def bfs(node):
    queue=deque()
    queue.append(node)
    visited[node]=True #방문 완료
    count = 0

    # print(f"[START] bfs 시작점: ({queue})")

    while queue:
        now = queue.popleft()

        for n in graph[now]: #해당 노드에 이웃한 노드
            # print(f"{n}번과 연결된 노드 : {graph[now]}")
            if not visited[n]: #아직 방문x
                visited[n] = True
                queue.append(n)
                count +=1 #노드 추가될 때 감염

    return count


print(bfs(1))


