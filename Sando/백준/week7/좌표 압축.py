#  * Author    : Kang San Ah
#  * Date      : 2025.06.11(Wed)
#  * Runtime   : 2 sec
#  * Memory    : 512 MB
#  * Algorithm : sort

# 1번째 풀이 -> 시간 초과, 단순히 N^2으로 풀면 안됨, 
# 문제를 보고 인덱스 순서라는 것을 파악 -> set + dict 조합으로 풀어야 함

# import sys 
# input = sys.stdin.readline

# n = int(input())
# a = list(map(int, input().split()))
# answer = []
# for i in range(n):
#     cnt = 0
#     tmp = a[i]
#     for j in range(n):
#         if a[i] > a[j] :
#             if a[j] != tmp :
#                 tmp = a[j]
#                 cnt += 1
    
#     answer.append(cnt)

# for i in answer:
#     print(i, end = ' ')

# -------

# 2번째 풀이
import sys 
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

sort_a = sorted(set(a)) # 중복 제거 + sort

coordinate = {value: idx for idx, value in enumerate(sort_a)}


for num in a:
    print(coordinate[num], end=' ')
