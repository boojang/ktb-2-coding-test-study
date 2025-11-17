'''
Author    : semi
Date      : 2025.11.17(Mon)
Runtime   : ms
Memory    : KB
Algorithm :
'''

import sys


input = sys.stdin.readline

n = int(input())

sort_list = []

for i in range(n):
    sort_list.append(int(input()))

sort_list.sort()
print(sort_list)





