# https://www.acmicpc.net/problem/14889

# * Author : Kang San Ah
# * Date : 2025.09.08(Mon)
# * Algorithm : data structure

import sys
input = sys.stdin.readline

N=int(input())
graph=[list(map(int,input().split())) for _ in range(N)]
arr=[]
arr2=[_ for _ in range(N)]
ansArr=[]
def cal_(a,b):
    asum=0
    for i in a:
        for j in a:
            if i==j:
                continue
            asum+=graph[i][j]
    bsum=0
    for i in b:
        for j in b:
            if i==j:
                continue
            bsum+=graph[i][j]
    ansArr.append(abs(asum-bsum))


def dfs():
    if len(arr)==N//2:
        #중복제거로직추가하기
        cal_(arr,list(set(arr2)-set(arr)))
        return
    
    for i in range(N):
        if len(arr)==0 or i >max(arr):
            arr.append(i)
            dfs()
            arr.pop()
dfs()
print(min(ansArr))