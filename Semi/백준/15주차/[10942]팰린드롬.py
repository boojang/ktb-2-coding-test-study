'''
Author    : semi
Date      : 2025.08.16(Sat)
Runtime   : 
Memory    : 
Algorithm : 
'''

# 자연수 n개 질문 m번
# [s,e]
# n개의 숫자 1 2 1 3 1 2 1
# s,e num[s-1] num[e-1] 1 3 0 1 2
# 팰린드롬이면 1 아니면 0 출력
import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
m = int(input())

for _ in range(m):
    ans = 1
    s,e = map(int,input().split())

    l = s-1
    r = e-1
    
    while l<r:
        if num[l] != num[r]:
            ans = 0
            break
        l +=1
        r -=1

    print(ans)

