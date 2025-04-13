'''
Author    : semi
Date      : 2025.04.13(Sun)
Runtime   : TLE
Memory    : TLE
Algorithm : Brute-force
'''

n = int(input())
nl = list(map(int,input().split()))

max_sum = float('-inf')
for i in range(n):
    for j in range(i,n):
        current_sum = sum(nl[i:j+1])
        max_sum = max(max_sum,current_sum)
        
print(max_sum)