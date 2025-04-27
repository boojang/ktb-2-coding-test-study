'''
Author    : semi
Date      : 2025.04.14(Mon)
Runtime   : 60ms
Memory    : 32412KB
Algorithm : 
'''


ans = []
count = 0

a = int(input())
for i in range(a):
    count = 0
    s = []
    s2 = []

    n, m = map(int, input().split())  # 총 갯수, 내가 원하는 아이의 위치
    s = list(map(int, input().split()))  # n개의 중요도

    s2 = [(priority, i == m) for i, priority in enumerate(s)]

    while True:
        current_max = max([item[0] for item in s2])
        if s2[0][0] == current_max and s2[0][1] == True:
            count += 1
            ans.append(count)
            break
        elif s2[0][0] == current_max: # 그냥 큰놈
            count +=1
            s2.pop(0)
        else:
            # count += 1
            first = s2.pop(0)
            s2.append(first)


for i in ans:
    print(i)


