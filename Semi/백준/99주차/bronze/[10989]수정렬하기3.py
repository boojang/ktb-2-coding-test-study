'''
Author    : semi
Date      : 2025.11.17(Mon)
Runtime   : ms
Memory    : KB
Algorithm :
'''

import sys


input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
count = [0] * 10001

for _ in range(n):
    i = int(input())
    count[i] +=1

for i in range(len(count)):
    if count[i] !=0:
        for _ in range(count[i]): #문자열을 곱하면 메모리 초과
            write(str(i) + '\n')



'''
* 메모리 사용 : sort_list에 천만개를 넣으면 메모리가 터진다.
* 카운팅 정렬
- 비교를 하지 않고 정렬하는 방법 
- 기존 정렬 -> 서로 값을 비교하고 순서를 바꾼다.
- 각 숫자가 몇 번 등장했는지 count 한다.
'''


