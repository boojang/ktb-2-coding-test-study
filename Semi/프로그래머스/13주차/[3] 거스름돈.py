'''
Author    : semi
Date      : 2025.08.06(Wed)
Runtime   : ms
Memory    : KB
Algorithm : DP
'''

def solution(n, money):
    mod = 1000000007 #overflow 방지

    dp = [0] * (n + 1)
    dp[0] = 1

    for coin in money:
        for i in range(coin, n + 1):
            dp[i] = (dp[i] + dp[i - coin]) % mod

    return dp[n]
