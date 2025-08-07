'''
Author    : semi
Date      : 2025.05.20(Wed)
Runtime   : 2508ms
Memory    : 32412KB
Algorithm :
'''

n,s = map(int,input().split())
number = list(map(int,input().split()))
total = 0
def backtracking(start,lst,num):

    if len(lst) == num:
        return 1 if sum(lst) ==s else 0

    count = 0
    for i in range(start,n):
        lst.append(number[i])
        count += backtracking(i + 1, lst, num)
        lst.pop()

    return count


# 갯수 정하기
for i in range(1,n+1):
    total += backtracking(0,[],i)

print(total)