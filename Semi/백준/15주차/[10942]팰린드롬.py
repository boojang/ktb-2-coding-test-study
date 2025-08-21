'''
Author    : semi
Date      : 2025.08.16(Sat)
Runtime   : 2260ms
Memory    : 63700KB
Algorithm : DP
'''
import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
m = int(input())

# n x n 리스트
# P[l][r] -> l부터 r 까지 배열이 팰린드롬인지 여부
# 어떻게 알 수 있을까? -> 배열의 길이를 사용해서 알 수 있겠다.
# room = [[]*n] -> 같은 주소 참조
# P = [[0 for _ in range(n)] for _ in range(n)]
P = [[False]*n for _ in range(n)]
ans = []

#★P[l][r] 을 알기 위해선 P[l+1][r-1]을 알고 있어야한다.
for length in range(1,n+1): # 길이 기준
    for l in range(0,n-length+1): # 시작인덱스 l 위치에서 length 만큼은 가야되니까
        r = l + length -1

        if length ==1 :
            P[l][r] = True
        else:
            P[l][r] = (num[r] == num[l]) and (length == 2 or P[l+1][r-1])


for _ in range(m):
    s,e = map(int,input().split())

    # print(1 if P[s-1][r-1] else 0)
    print(int(P[s-1][e-1]))
    # ans.append(str(int(P[s-1][e-1])))

# print("\n".join(ans))

'''
for l in range(0,n):
    for r in range(0,n):
        # 앞선 애들은 넣으면 안된다. 하지만 index를 위해서 채워야함 -> 걍 기본을 0으로 채워넣기
        # if l>=r:
        #     P[l][r].append(-1)
        #     continue
        if r==l: #길이=1
            P[l][r] = 1
        elif r-l == 1: #길이=2
            if num[r] == num[l]:  # 11,22,33
                P[l][r] = 1
        elif r-l == 2: #길이=3
            if num[r] == num[l]:  # 121,212,313
                P[l][r] = 1
        else: #길이=4 이상 # 1221 1441 2313
            # (r-l+1)//2 번 비교해야한다.
            # r l 이 같은지 -> r-1 l-1이 같은지 -> 이걸 이전 데이터를 사용해서 알 수 있나?
            # P[l-1][r-1]을 사용해서 식을 어떻게 세우지
            continue
'''