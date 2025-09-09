'''
Author    : semi
Date      : 2025.09.09(Tues)
Runtime   : ms
Memory    :
Algorithm :
'''

# 총 n명
# n 짝수
# 1~n 사람수
# Sij i번 사람과 j번 사람의 능력치

# Sij 합의 차이가 최소화

import sys
from itertools import combinations


input = sys.stdin.readline

s=[]
sum_1,sum_2=0,0
total_sum = float('inf')

n = int(input())

for i in range(n):
   s.append(list(map(int,input().split())))

for s1 in combinations(range(n),n//2):
    # print(f"s1 = { s1 }")
    s2 = set(range(n)) - set(s1)
    # print(f"s2 = { s2 }")

    for a,b in combinations(s1,2):
        sum_1 += s[a][b]+s[b][a]

    for c,d in combinations(s2,2):
        sum_2 += s[c][d]+s[d][c]

    total_sum = min(total_sum,abs(sum_1-sum_2))
    
    # print(f"sum_1,sum_2 = { sum_1,sum_2 }")
    # print(f"total_sum = {total_sum}")
    sum_1,sum_2=0,0

print(total_sum)