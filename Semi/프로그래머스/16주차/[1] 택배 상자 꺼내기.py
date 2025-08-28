'''
https://school.programmers.co.kr/learn/courses/30/lessons/389478
Author    : semi
Date      : 2025.08.27(Wed)
Algorithm : 구현
'''

def solution(n, w, num):
    col = 0
    row = 0
    box_cn = 1

    # 행 구하기
    if num % w ==0:
        row = num//w
    else:
        row = (num//w) + 1

    # 열 구하기
    if row % 2 == 1 : #홀수 (순행)
        if num % w == 0:
            col = num // row
        else:
            col = num % w

    else: # 짝수 역행)
        if num % w == 0:
            col = 1
        else:
            col = (w+1)-(num % w)

    # 위에 있는 상자갯수 구하기
    while True:
        jump = 0

        if row % 2 ==1: #홀수
            jump = 2*w - (2*col-1)
        else: #짝수
            jump = 2*col-1

        num += jump
        if num > n: #조심
            break
        box_cn += 1
        row += 1

    return box_cn



print(solution(22,6,12))