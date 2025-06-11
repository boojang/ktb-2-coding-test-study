#  * Author    : Kang San Ah
#  * Date      : 2025.06.11(Wed)
#  * Runtime   : 1 sec
#  * Memory    : 256 MB
#  * Algorithm : Brute-force

import sys 
from itertools import permutations
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
answer = 0

for p in permutations(a):
    total = 0
    for i in range (n-1):
        total += abs(p[i] - p[i+1])
        answer = max(total, answer)
        
print(answer)