# https://www.acmicpc.net/problem/14501

# * Author : Kang San Ah
# * Date : 2025.09.08(Mon)
# * Algorithm : dp
import sys
input = sys.stdin.readline

n = int(input())

ls = []
for _ in range(n):
    ls.append(list(map(int, input().split())))
dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1): # 거꾸로
    if i + ls[i][0] > n: # 상담에 필요한 일수가 퇴사일을 넘어가면 전날로 가기
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], ls[i][1] + dp[i + ls[i][0]])

print(dp[0])