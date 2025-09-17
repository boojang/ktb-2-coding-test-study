'''
Author    : semi
Date      : 2025.09.09(Tues)
Runtime   : ms
Memory    :
Algorithm :
'''

import sys
from itertools import combinations


input = sys.stdin.readline

s=[]
sum_1,sum_2=0,0
total_sum = float('inf')

n = int(input())

for i in range(n):
   s.append(list(map(int,input().split())))

# (+수정) 전체 집합을 두개의 동일한 그룹으로 나눌 때 기준이 되는 요소를 고정시킨다.
# -> 경우의 수를 줄일 수 있음
for s1 in combinations(range(1,n),n//2-1):
    s1 = list(s1)
    s1.append(0)
    s2 = set(range(n)) - set(s1)

    for a,b in combinations(s1,2):
        sum_1 += s[a][b]+s[b][a]

    for c,d in combinations(s2,2):
        sum_2 += s[c][d]+s[d][c]

    total_sum = min(total_sum,abs(sum_1-sum_2))
    sum_1,sum_2=0,0

print(total_sum)