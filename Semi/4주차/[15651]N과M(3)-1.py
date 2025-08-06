'''
Author    : semi
Date      : 2025.05.20(Tues)
Runtime   : 1836ms
Memory    : 32412KB
Algorithm : BackTracking
'''

n,m=map(int,input().split())

sequence = []

def backtracking():
    
    if len(sequence) == m:
        print(*sequence)
        return
    
    for i in range(1,n+1): #기준이 된다.
        sequence.append(i)
        backtracking()
        sequence.pop()

backtracking()