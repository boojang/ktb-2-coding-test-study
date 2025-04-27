'''
Author    : semi
Date      : 2025.04.12(Sat)
Runtime   : 7196ms
Memory    : 33192KB
Algorithm : Dynamic Programming
'''

# approach #1
# Greedy한방식 : 가장 큰 제곱수 부터 가능한 한 최대한 많이 쓰고 나머지를 채우는 방식
# ex) 11 -> 가장 큰 제곱 수 9 -> 11 = 9 =2 -> 11 = 3^2 + 1^2 + 1^2 
# Problem : 항상 최소를 보장하지 않는다. ex) 12 


# approach #2
# Dynamic Programming
n = int(input())

#dp : i를 제곱수의 합으로 나타내는 필요한한 '최소' 항의 개수를 저장
# 초기값 : 무한대로 설정
dp = [float('inf')]*(n+1)
# 0을 표현하는데 필요한 항 = 0개
dp[0] = 0


#dp 배열 채우기 (bottom-up)
for i in range(1,n+1):
    j = 1
    while j*j <= i:
        dp[i] = min(dp[i],dp[i-j*j]+1)
        # print(f"i ={i}, j={j}")
        # print(f"dp[{i}]={dp[i]}")
        j +=1

print(dp[n])
        
        
    