from functools import cmp_to_key
# cmp_to_key
def compare(a,b):
    if int(str(a)+str(b)) > int(str(b)+str(a)):
        return -1 # a가 앞  -> 그 2개의 숫자를 어떻게 정렬 할 것인가? -> 내림차순
    elif int(str(a)+str(b)) < int(str(b)+str(a)):
        return 1 # b가 앞 -> 오름 차순
    else:
        return 0

# 입력 = list 값 -> def로 만든다
def solution(numbers):
    numbers = sorted(numbers, key=cmp_to_key(compare))
    answer = ''.join(map(str, numbers))
    # 예외처리: 0이 여러개일 경우 '0'만 남기기
    if answer[0] == '0':
        return '0'
    return answer