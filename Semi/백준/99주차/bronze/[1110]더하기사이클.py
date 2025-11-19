'''
Author    : semi
Date      : 2025.11.17(Mon)
Runtime   : 36ms
Memory    : 32544KB
Algorithm :
'''


# 사이클의 길이

N = int(input())

answer=0
cycle = N

while True:
    a = cycle // 10 #앞자리
    b = cycle % 10 #뒷자리
    c = (a+b) % 10 #뒷자리

    cycle = int(str(b)+str(c))

    answer +=1
    if N == cycle :
        break

print(answer)