'''
Author    : semi
Date      : 2025.04.13(Sun)
Runtime   : 39096ms
Memory    : 84KB
Algorithm : Kadane's Algorithm
'''

n = int(input())
nl = list(map(int,input().split()))

max_sum= current_sum = nl[0]

for i in range(1,n):
    current_sum = max(nl[i],current_sum+nl[i])
    max_sum = max(max_sum,current_sum)
    
print(max_sum)

