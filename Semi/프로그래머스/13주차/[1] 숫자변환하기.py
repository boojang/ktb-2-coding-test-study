'''
Author    : semi
Date      : 2025.08.05(Tues)
Runtime   : ms
Memory    : KB
Algorithm : BFS
'''

# x +n
# x *2
# x *3

#방법을 선택하기 전 원래 상태 or 최소 선택
from collections import deque

def solution(x, y, n):
    # 지금까지 계산 과정?
    # x -> y
    num = []
    queue = deque() #다음에 방문할 노드
    queue.append((x,0))
    visited = {} # 방문기록. set : 특정 요소 여부를 빠르게 확인할 수 있다.


    # BFS
    while queue: # 큐가 빌 때까지 반복
        current_num,count = queue.popleft()

        if current_num == y:
            return count

        # 연산1
        next_num1 = current_num +n
        if next_num1 <= y and next_num1 not in visited:
            visited.add(next_num1)
            queue.append((next_num1,count+1))

        # 연산2
        next_num2 = current_num *2
        if next_num2 <= y and next_num2 not in visited:
            visited.add(next_num2)
            queue.append((next_num2,count+1))

        # 연산3
        next_num3 = current_num * 3
        if next_num3 <= y and next_num3 not in visited:
            visited.add(next_num3)
            queue.append((next_num3, count + 1))

    #탐색 종료
    return -1
