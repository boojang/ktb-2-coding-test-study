'''
Author    : semi
Date      : 2025.11.19(Wed)
Runtime   : 32412ms
Memory    : 36KB
Algorithm :
'''
from itertools import combinations

child = [int(input()) for _ in range(9)]

total = sum(child)

for i in range(len(child)):
    for j in range(i,len(child)):
        if total - child[i] - child[j] == 100:
            answer = [child[k] for k in range(len(child)) if k!=i and k!=j]
            answer.sort()
            print(*answer)
            exit()
