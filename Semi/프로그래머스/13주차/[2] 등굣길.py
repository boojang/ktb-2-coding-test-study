'''
Author    : semi
Date      : 2025.08.06(Wed)
Runtime   : ms
Memory    : KB
Algorithm :
'''

def solution(m, n, puddles):
    mod = 1000000007 #overflow 방지
    
    # dp 배열  (0-indexed)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 물에 잠긴 지역 표시
    for x, y in puddles:
        dp[y][x] = -1 

    # 시작
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:  # 물에 잠긴 곳은 경로 0
                dp[i][j] = 0
                continue
            if i == 1 and j == 1:
                continue  # 시작점은 이미 처리

            # 위에서 오는 경로
            if dp[i-1][j] != -1:
                dp[i][j] += dp[i-1][j]
            # 왼쪽에서 오는 경로
            if dp[i][j-1] != -1:
                dp[i][j] += dp[i][j-1]
            dp[i][j] %= mod

    return dp[n][m]
