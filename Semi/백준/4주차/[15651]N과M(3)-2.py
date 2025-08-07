'''
Author    : semi
Date      : 2025.05.20(Tues)
Runtime   : 964ms
Memory    : 32412KB
Algorithm : BackTracking
'''
#I/0 수정
import sys
n, m = map(int, sys.stdin.readline().split())
sequence = []

def backtracking():
    if len(sequence) == m:
        sys.stdout.write(" ".join(map(str, sequence)) + "\n")
        return
    for i in range(1, n+1):
        sequence.append(i)
        backtracking()
        sequence.pop()

backtracking()