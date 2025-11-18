'''
Author    : semi
Date      : 2025.11.18(Tues)
Runtime   : 300ms
Memory    : 36080KB
Algorithm :
'''
import sys
import math

input = sys.stdin.readline

A,B,V = map(int,input().split())

answer = math.ceil((V-A) / (A-B))

print(answer +1)



'''
- V 최대 : 10억 -> while문 10억 반복
- while을 안쓰고 계산할 수 있는 방법
- (A-B) : 하루동안 갈 거리 (순증가량)
- 근데 A에서 V에 도착할것도 고려해야함
- *V-A : 마지막 날 낮에 도착하기 직전 높이
- *마지막날- 낮만 고려/ 그 전날 - (A-B)씩 증가
'''