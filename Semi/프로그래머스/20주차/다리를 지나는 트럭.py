'''
https://school.programmers.co.kr/learn/courses/30/lessons/42583
Author    : semi
Date      : 2025.09.25(Thurs)
Algorithm :
'''
# 다리 위에는 동시에 bridge_length 만큼의 트럭만 올라갈 수 있다.
# 다리 위에 있는 트럭들의 무게 합은 weight를 초과할 수 없다
from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    time = 0
    bridge = deque([])
    while truck_weights:
        if sum(bridge)<weight:
            #pop해
            bridge.append(truck_weights.popleft())
        if len(bridge)<bridge_length:
            #pop해서 넣어
            bridge.append(truck_weights.popleft())

        time +=1

    return time