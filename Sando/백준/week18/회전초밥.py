# https://www.acmicpc.net/problem/2531

# * Author : Kang San Ah
# * Date : 2025.09.08(Mon)
# * Algorithm : sliding window

import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr2 = []
result = 0
for i in range(n):
    rice = arr[i : i + k]
    if i + k > n:
        rice = arr[i:] + arr[:k - (n - i)]
    rice += [c]
    result = max(result, len(set(rice)))

print(result)