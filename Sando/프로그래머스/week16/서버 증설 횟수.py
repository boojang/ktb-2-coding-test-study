# https://school.programmers.co.kr/learn/courses/30/lessons/150370?language=python3

# * Author : Kang San Ah
# * Date : 2025.08.27(Wed)
# * Algorithm : sliding window

from heapq import heappush, heappop 

def solution(players, m, k):
    n = len(players)
    answer = 0
    heap = []  # 서버 반납 시각 저장
    active = 0  # 현재 운영 중 서버 수

    for t in range(n):
        while heap and heap[0] == t:
            heappop(heap)
            active -= 1

        need = players[t] // m

        if need > active:
            add = need - active
            answer += add
            active += add
            for _ in range(add):
                heappush(heap, t + k)

    return answer


players = [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5]
m = 3
k = 5

print(solution(players, m, k))  
