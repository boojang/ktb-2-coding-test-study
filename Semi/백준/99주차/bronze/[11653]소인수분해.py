'''
Author    : semi
Date      : 2025.11.20(Thurs)
Runtime   : ms
Memory    : KB
Algorithm :
'''


N = int(input())

i=2
while i*i <=N:
    while N % i ==0:
        print(i)
        N //= i

    i+=1

# 마지막 값이 1보다 크면 소수 2 3 5 7..
if N >1:
    print(N)