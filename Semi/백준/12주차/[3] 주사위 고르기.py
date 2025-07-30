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
        print(f"a_idx:{a_idx}, b_idx:{b_idx}")

        # 주사위 조합 구하기
        a_dice = [dice[i] for i in a_idx]
        b_dice = [dice[i] for i in b_idx]

        # 주사위 합 조합 구하기
        a_cases = list(product(*a_dice))
        a_sums = [sum(comb) for comb in a_cases]
        a_counter = Counter(a_sums)
        # a_sums.sort()

        b_cases = list(product(*b_dice))
        b_sums = [sum(comb) for comb in b_cases]
        b_counter = Counter(b_sums)
        # b_sums.sort()


        print(f"A가 고른 주사위: {a_dice}")
        print(f"B가 고른 주사위: {b_dice}")
        print(f"A의 가능한 조합: {a_cases[:5]} ...")  # 너무 많으면 일부만 출력
        print(f"B의 가능한 조합: {b_cases[:5]} ...")
        print(f"a_sums: {a_sums}")
        print(f"b_sums: {b_sums}")
        print(f"a_counter: {a_counter}")
        print(f"b_counter: {b_counter}")

        for key,value in a_counter.items():
            print(key,value)
            # print([if b_counter[i] < key for i in range(len(b_counter))])
            count = sum(b_val for b_key, b_val in b_counter.items() if b_key<key)
            total += count * value # key보다 작은 경우 * x가 나온 횟수
            print(f'count:{count}')
            print(f'total:{total}')
        if total > max_win:
            max_win = total
            answer = a_idx
        print('-'*40)

    return [i+1 for i in answer]

# dice = [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]
dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]

print(solution(dice))



