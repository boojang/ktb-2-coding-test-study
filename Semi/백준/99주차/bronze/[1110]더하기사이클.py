'''
Author    : semi
Date      : 2025.11.17(Mon)
Runtime   : 300ms
Memory    : 36080KB
Algorithm :
'''


# 사이클의 길이

N = input()

answer=0
cycle = N

while True:

    if len(cycle) == 1:
        a,b = '0',cycle
    else:
        a,b = cycle[0],cycle[1]

    print(f"a,b = { a,b }")
    c = str(int(a) + int(b))
    print(f"c = { c }")

    if len(c) == 1:
        a,b = '0',c
        cycle = cycle[1] + c
    else:
        a,b = c[0],c[1]
        cycle = cycle[1] + c[1]


    print(f"cycle = { cycle }")

    answer +=1

    if cycle == N:
        break

print(answer)