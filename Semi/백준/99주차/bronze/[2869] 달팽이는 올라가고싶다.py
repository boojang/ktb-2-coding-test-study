'''
Author    : semi
Date      : 2025.11.18(Tues)
Runtime   : 300ms
Memory    : 36080KB
Algorithm :
'''
import sys

input = sys.stdin.readline

A,B,V = map(int,input().split())

cur = 0
day = 1

while cur < V:
    #낮
    cur +=A

    if(cur >= V):
        break
    #밤
    cur -=B

    day += 1

print(day)

# day1 2 -1 = 1
# day2 3 -1 = 2
# day3 4 -1 = 3
# day4 5 -> 끝