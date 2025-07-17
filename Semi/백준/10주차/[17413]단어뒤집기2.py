'''
Author    : semi
Date      : 2025.07.12(Sat)
Runtime   : 212ms
Memory    : 33192KB
Algorithm : 
'''

import sys
input = sys.stdin.readline

# readline은 마지막에 \n이 포함됨
n = input().rstrip()

stack = []
result=''
i=0

while i != len(n):
    if n[i] == '<':
        while stack:
            result += stack.pop()
        while n[i] != '>':
            result += n[i]
            i+=1
        result += '>'
    elif n[i] == ' ':
        while stack:
            result += stack.pop()
        result += ' '
    else:
        stack.append(n[i])
    i+=1
else:
    while stack:
        result += stack.pop()

print(result)