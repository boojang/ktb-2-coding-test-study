from itertools import combinations_with_replacement
from heapq import heappush, heappop, heapify

def get_mento_combination(k, n):
    type_mento = []
    for case in combinations_with_replacement(range(k), r=n-k):
        mento_count = [1] * k
        for idx in case:
            mento_count[idx] += 1
        type_mento.append(mento_count)
    return type_mento

def solution(k, n, reqs):
    type_mento = get_mento_combination(k, n)
    time = float('inf')

    for case in type_mento:
        wait_time_sum = 0
        mento_end_time = [[0] * cnt for cnt in case]
        for i in range(len(case)):
            heapify(mento_end_time[i])

        for a, b, c in reqs:
            idx = c - 1
            earliest_end = heappop(mento_end_time[idx])
            start_time = max(earliest_end, a)
            wait_time_sum += start_time - a
            heappush(mento_end_time[idx], start_time + b)

        time = min(time, wait_time_sum)
    return time

# 테스트
k = 3
n = 5
reqs = [
    [10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3],
    [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]
]
print(solution(k, n, reqs))
