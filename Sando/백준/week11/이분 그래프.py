# https://www.acmicpc.net/problem/1520

# * Author : Kang San Ah
# * Date : 2025.07.21(Mon)
# * Runtime : 2 sec
# * Memory : 256 MB
# * Algorithm : Tree + DFS

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

isEven = True

def DFS(node):
    global isEven # global scope
    visited[node] = True
    for i in a[node] :
        if not visited[i]:
            chk[i] = (chk[node]+1)%2
            DFS(i)
        elif chk[node] == chk[i]:
            isEven = False    

n = int(input())

for _ in range(n):
    v,e = map(int, input().split())
    a = [[]for _ in range(v+1)]
    visited = [False] * (v+1)
    chk = [0] * (v+1)
    isEven = True
    
    for i in range(e):
        start, end = map(int, input().split())
        a[start].append(end)
        a[end].append(start)
        
    for i in range(1, v+1):
        if isEven :
            DFS(i)
        else :
            break
    
    print("YES" if isEven else "NO")
    