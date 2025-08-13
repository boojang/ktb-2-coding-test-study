'''
Author    : semi
Date      : 2025.08.08(Fri)
Runtime   : ms
Memory    : KB
Algorithm : -
'''
from itertools import product,combinations_with_replacement
from heapq import heappush,heappop,heapify

# w_t(m) : 멘토가 m명일 때 총 대기시간
# 남는 멘토 n-k명을 한 명씩 배분하되, 매 스텝
# 이득 Δ_t = W_t(m) - W_t(m+1) 가 가장 큰 유형에 1명 추가하는 그리디.
def wait_sum_for_type(requests):
    return

def build_request_by_type(k,reqs):
    by_type = [[] for _ in range(k)]
    for a,b,c in reqs:
        by_type[c-1].append((a,b))

    return by_type



# 경우의 수 만들어주기
# 멘토의 리스트 x -> 각 유형별 멘트 `수`
def get_mento_combination(k,n):

    type_mento = []


    # 중복 조합
    # case : (0,0,1,1,2,2) -> 0번 유형 멘토 2명, 1번 유형 멘토 2명, 2번 유형 멘토 2명
    # case 순서는 상관 없음 -> 인덱스가 유형을 의미하는게 아니라 값이 유형을 의미한다.
    for case in combinations_with_replacement(range(k),r=n-k) :
        mento_count = [1] * k
        for idx in case:
            mento_count[idx] +=1
        type_mento.append(mento_count)

    return type_mento


def solution(k, n, reqs):
    type_mento = get_mento_combination(k,n)

    time = float('inf')

    # 각 케이스 별로 시뮬레이션
    # 멘토의 상담종료 시간을 관리해야한다.
    for case in type_mento:
        # print(f"-----------테스트 case: {case}-----------")
        wait_time_sum = 0

        # ★유형별 멘토별 상담 끝나는 시간 관리
        mento_end_time = [[0] * cnt for cnt in case]
        print(f"mento_end_time = { mento_end_time }")

        #각 유형별로 heapify -> 1차원 하나씩 heapify
        for i in range(len(case)):
            heapify(mento_end_time[i])

        for a,b,c in reqs:
            idx = c-1 # 0-indexed

            # 가장 빨리 끝나는 멘토 index find
            earliest_end = heappop(mento_end_time[idx])

            # 시간 비교 (끝나는 시간 vs 도착한 시간)
            # ★ 더 늦은 시간이 실제 상담 시작 시간
            start_time = max(earliest_end,a)

            # 대기시간 누적
            wait_time_sum += start_time - a

            # 다음에 상담할 수 있는 시간 갱신
            heappush(mento_end_time[idx],start_time+b)
            '''
            min_time = float('inf')
            min_idx = -1
            for i in range(len(mento_end[idx])):
                if mento_end[idx][i] < min_time:
                min_time = mento_end[idx][i]
                min_idx = i
            '''
        time = min(time, wait_time_sum)

    return time


k = 3
n = 5
# a : 온 시간 b : 걸리는 시간 c : 유형
reqs = [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]

solution(k,n,reqs)