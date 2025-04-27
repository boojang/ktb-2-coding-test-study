'''
Author    : semi
Date      : 2025.04.27(Sun)
Runtime   : 184ms
Memory    : 36016KB
Algorithm :
'''

from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

def bfs(node):
    queue=deque()
    queue.append(node)
    visited[node]=True
    count = 0


    while queue:
        now = queue.popleft()

        for n in graph[now]: 
            if not visited[n]: 
                visited[n] = True
                queue.append(n)
                count +=1 

    return count


print(bfs(1))


