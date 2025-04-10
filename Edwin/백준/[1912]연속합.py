'''
Author    : edwin
Date      : 2024.04.07(Mon)
Runtime   : 84 ms
Memory    : 39096 KB
Algorithm : DP
'''

import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

max_val = lst[0]
now_sum = lst[0]

for i in range(1, N):
    now_sum = max(lst[i], lst[i] + now_sum)
    max_val = max(max_val, now_sum)
print(max_val)