'''
https://school.programmers.co.kr/learn/courses/30/lessons/42576
Author    : semi
Date      : 2025.09.30(Tues)
Algorithm :
'''

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



'''
#problem : set은 집합이므로 중복으로 저장하지 않는다.
#bad-case : ["mislav", "stanko", "mislav", "ana"], 	["stanko", "ana", "mislav"]
def solution1(participant, completion):
    parti = set(participant)
    comp = set(completion)
    not_comp = parti - comp
    not_comp = list(not_comp)
    print(f"not_comp = { not_comp }")
    return not_comp[0]

#problem : 중복되는 이름이 있을 경우 통과해버린다.
#bad-case : ["mislav", "stanko", "mislav", "ana"], 	["stanko", "ana", "mislav"]
def solution2(participant, completion):
    answer = []
    for i in participant:
        print(f"i = { i }")
        if i not in completion:
            answer.append(i)

    print(f"answer = { answer }")
    return
'''