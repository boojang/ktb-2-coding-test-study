'''
Author    : semi
Date      : 2025.09.08(Mon)
Runtime   : 32412ms
Memory    : 44ms
Algorithm : brute force
'''
import sys

input = sys.stdin.readline

N = int(input())

sch = []
money=[0]*(N+1)

for i in range(N):
    T,P = map(int,input().split())
    sch.append((T,P))

for i in range(N):
    t,m = sch[i][0],sch[i][1]

    # 상담을 안 하는 경우
    if i>0:
        money[i] = max(money[i],money[i-1])

    # 상담을 하는 경우
    if i + t <= N:
        money[i+t]=max(money[i+t],sch[i][1] + money[i])

#최댓값
print(max(money))