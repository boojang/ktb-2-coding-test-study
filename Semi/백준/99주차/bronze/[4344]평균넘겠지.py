'''
Author    : semi
Date      : 2025.11.18(Tues)
Runtime   : 36ms
Memory    : 32412KB
Algorithm :
'''
import sys

input = sys.stdin.readline

C = int(input())

for _ in range(C):
    std = list(map(int,input().split()))
    score = std[1:]
    avg = sum(score) / (len(score))
    score_count = [sc for sc in score if sc>avg]
    ratio = round(len(score_count) / len(score) *100,3)
    print(f"{ratio}%")
    
    
'''
- 미리 전처리하기
'''