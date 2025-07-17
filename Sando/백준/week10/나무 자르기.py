# https://www.acmicpc.net/problem/2805

# * Author : Kang San Ah
# * Date : 2025.07.14(Mon)
# * Runtime : 1 sec
# * Memory : 256 MB
# * Algorithm : binary search 

n, m = map(int, input().split())

a = list(map(int, input().split()))

L = 1 # 제일 작은 수
R = max(a) # 제일 큰 수

answer = 0
while L <= R :
    sum = 0
    mid = (L+R) // 2
    for num in a:
        if num >= mid:
            sum += num - mid 
    if sum >= m :
        answer = mid
        L = mid + 1
    elif sum < m :
        R = mid - 1

print(answer)
