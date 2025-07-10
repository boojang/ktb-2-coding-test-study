#  * Author    : Kang San Ah
#  * Date      : 2025.07.04(Fri)
#  * Runtime   : 1 sec
#  * Memory    : 256 MB
#  * Algorithm : DFS


# 인접 리스트로 만들어서
# 첫 번째 요소만 반환하면 됨
import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
answer = [0 for _ in range(n+1)] # [0,0,0 ... n+1개]
a =[[0]for _ in range(n+1)] # [[0], [0] ... n+1개]
parent = [0 for _ in range(n+1)]


def DFS(current, x):
    parent[current] = x
    for nxt in a[current]:
        if parent[nxt] == 0:
            DFS(nxt, current)
    
# 인접 리스트 데이터 삽입
for i in range(n-1):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

DFS(1, 0)

for i in range(2, n+1):
    print(parent[i])


