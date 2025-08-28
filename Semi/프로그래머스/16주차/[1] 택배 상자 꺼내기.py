'''
https://school.programmers.co.kr/learn/courses/30/lessons/389478
Author    : semi
Date      : 2025.08.27(Wed)
Algorithm : 구현
'''

def solution(n, w, num):

    # 개선된 코드
    # 1~n 범위를 0~(n-1) 범위로 변환
    row = (num - 1) // w + 1

    # 개선된 코드
    temp_col_from_zero = (num-1) % w # 0부터 시작
    print(f"temp_col_from_zero = { temp_col_from_zero }")

    # 열 구하기
    if row % 2 == 1 : #홀수
        col = temp_col_from_zero + 1
    else: # 짝수
        col = w-temp_col_from_zero
    
    print(f"row,col = { row,col }")

    # 위에 있는 상자갯수 구하기
    box_cn = 1
    while True:
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