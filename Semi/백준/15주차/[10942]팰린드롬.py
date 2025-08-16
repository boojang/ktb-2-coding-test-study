'''
Author    : semi
Date      : 2025.08.16(Sat)
Runtime   : 
Memory    : 
Algorithm : 
'''

# 자연수 n개 질문 m번
# [s,e]
# n개의 숫자 1 2 1 3 1 2 1
# s,e num[s-1] num[e-1] 1 3 0 1 2
# 팰린드롬이면 1 아니면 0 출력

n = int(input())
num = list(map(int,input().split()))
m = int(input())

for _ in range(m):
    ans = 1
    s,e = map(int,input().split())

    spl = num[s-1:e]
    nspl = len(spl)
    # print(f"spl = { spl }")
    for i in range(0,nspl):
        # 아닌경우는 ans = 0으로 바꾸기
        
        # print(f"spl[i] = {spl[i]}, spl[n-1] = {spl[nspl-1 - i]}")

        if nspl % 2 != 0: # 가운데 숫자 제외
            if i != nspl//2:
                if spl[i] != spl[nspl-1-i]:
                    ans = 0
        else:
            if spl[i] != spl[nspl-1-i]:
                ans = 0
    print(ans)

