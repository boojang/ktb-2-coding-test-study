'''
Author    : semi
Date      : 2025.11.19(Wed)
Runtime   : 32412ms
Memory    : 36KB
Algorithm :
'''
from itertools import combinations

child = [int(input()) for _ in range(9)]

for comb in combinations(child,7):
    if sum(comb) == 100:
        answer = sorted(comb)
        print(*answer)
        break