'''
Author    : semi
Date      : 2025.08.08(Fri)
Runtime   : ms
Memory    : KB
Algorithm : -
'''
from itertools import product
import heapq
# 멘토 n 명 1~k 유형
# k개 상담 유형 중 하나만 담당
# t = 상담 시작 t - 상담 요청 t
# 상담 시작 t(끝나는 t) = 앞 시간 + 상담시간

# 멘토 인원을 적절히 배정 (최소가 되는) -> 상담을 받기까지 기다린 시간을 모두 합한 값

# n에게 k유형을 배정해야함
# k개는 자동으로 정해짐 n-k개를 뭐로 정의하는가? -> 최대 5개영역, 20명 멘토. 5^15 계산 가능?
# n은 지금 상담 중인가? 언제 상담이 끝나는가?
# 최소를 계산하려면 알고리즘이 필요한가? -> 경우를 어떻게 나눌까 이게 제일 문제다.

# 1인 사람이 바로 가능한가? -> 불가능 판단 : (a+b) > a`(뒤에 들어온사람) -> 대기시간 (a+b) - a`
# 멘토에게 저장해야할것 -> 지정된 k 유형 + 끝나는 시간

# 경우의 수 만들어주기
# 멘토의 리스트 x -> 각 유형별 멘트 `수`
def get_mento_combination(k,n):
    # k개 있고 (n-k)개 의 combination을 알아야함
    # [1~k]가 있어
    # mento = [a for a in range(1,k+1)]
    type_mento = []

    #중복 순열
    for case in product(range(k),repeat=n-k) :
        mento_count = [1] * k
        for idx in case:
            mento_count[idx] +=1

        type_mento.append(mento_count)
        print(type_mento)

    return type_mento

def solution(k, n, reqs):
    type_mento = get_mento_combination(k,n)
    time = float('inf')

    # 각 케이스 별로 시뮬레이션
    # 멘토의 상담종료 시간을 관리해야한다.
    for case in type_mento:
        print(f"-----------테스트 case: {case}-----------")
        wait_time_sum = 0
        # ★유형별 멘토별 상담 끝나는 시간 관리
        mento_end_time = [[0]*cnt for cnt in case]

        for a,b,c in reqs:
            idx = c-1 # 0-indexed
            print(f"c: {c}")
            print(f"mento_end_time: {mento_end_time[idx]}")
            # 가장 빨리 끝나는 멘토 index find
            min_idx = mento_end_time[idx].index(min(mento_end_time[idx]))

            # 시간 비교 (끝나는 시간 vs 도착한 시간)
            # ★ 더 늦은 시간이 실제 상담 시작 시간
            start_time = max(mento_end_time[idx][min_idx],a)

            # 대기시간 누적
            wait_time_sum += start_time - a
            print(f"wait_time_sum: {wait_time_sum}")

            # 다음에 상담할 수 있는 시간 갱신
            mento_end_time[idx][min_idx] = start_time + b

            print(f"min_idx: {min_idx}")
            '''
            min_time = float('inf')
            min_idx = -1
            for i in range(len(mento_end[idx])):
                if mento_end[idx][i] < min_time:
                min_time = mento_end[idx][i]
                min_idx = i
            '''
        time = min(time, wait_time_sum)
        print(f"최소시간: {time}")

    return time


k = 3
n = 5
# a : 온 시간 b : 걸리는 시간 c : 유형
reqs = [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]

solution(k,n,reqs)