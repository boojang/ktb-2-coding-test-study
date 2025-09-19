# https://school.programmers.co.kr/learn/courses/30/lessons/42842

# * Author : Kang San Ah
# * Date : 2025.09.17(Wed)
# * Algorithm : 구현

def solution(brown, yellow):
    answer = []
    total = brown + yellow # 12
    for height in range(3,total):
        if total % height != 0:
            continue 
        width = total // height  # 4
        if (width -2) * (height - 2) == yellow: # 2
            return [width, height]