'''
Author    : semi
Date      : 2025.07.29(Tues)
Runtime   : ms
Memory    : KB
Algorithm :
'''

from itertools import combinations,product
from collections import Counter

def solution(dice):
    n = len(dice)
    idx = list(range(n)) # 인덱스로 접근
    max_win = 0
    answer = []



    # 주사위 조합 -> 인덱스로 접근
    for comb in combinations(idx,n//2):
        total = 0
        a_idx = set(comb)
        b_idx = set(idx) - a_idx

        # 주사위 조합 구하기
        a_dice = [dice[i] for i in a_idx]
        b_dice = [dice[i] for i in b_idx]

        # 주사위 합 조합 구하기
        a_cases = list(product(*a_dice))
        a_sums = [sum(comb) for comb in a_cases]
        a_counter = Counter(a_sums)

        b_cases = list(product(*b_dice))
        b_sums = [sum(comb) for comb in b_cases]
        b_counter = Counter(b_sums)

        # 조합별로 A가 이길 경우의 수
        for key,value in a_counter.items():

            count = sum(b_val for b_key, b_val in b_counter.items() if b_key<key)
            total += count * value # key보다 작은 경우 * x가 나온 횟수
        
        if total > max_win:
            max_win = total
            answer = a_idx

    return [i+1 for i in answer]


