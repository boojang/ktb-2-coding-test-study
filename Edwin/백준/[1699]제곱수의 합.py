N = int(input())
dp = [0] * (N + 1)

for i in range(1, N + 1):
    min_cnt = float('inf')
    j = 1
    while j*j <= i:
        min_cnt = min(min_cnt, dp[i- j*j] + 1)
        j += 1
    dp[i] = min_cnt
print(dp[N])