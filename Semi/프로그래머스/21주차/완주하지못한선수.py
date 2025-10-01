'''
https://school.programmers.co.kr/learn/courses/30/lessons/42576
Author    : semi
Date      : 2025.09.30(Tues)
Algorithm :
'''
from collections import Counter

def solution_efficient(participant, completion):

    # 1. 참여자 :(name:count) Counter로 등장횟수 자동 계산
    parti_dict = Counter(participant)

    # 2. 완주자 :Counter로 등장횟수 자동 계산
    compl_dict = Counter(completion)

    # 3. 완주하지 못한 사람
    not_compl = parti_dict - compl_dict

    return list(not_compl.keys())[0]

def solution(participant, completion):
    parti_dict = {}

    # 1.사전에 추가 (name:count)
    for name in participant:
        if name in parti_dict:
            parti_dict[name] +=1
        else:
            parti_dict[name] =1

    # 2. completion 제거
    for name in completion:
        if name in parti_dict:
            parti_dict[name] -=1

    # 3. return
    for name,value in parti_dict.items():
        if value == 1:
            return name

solution_efficient(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])