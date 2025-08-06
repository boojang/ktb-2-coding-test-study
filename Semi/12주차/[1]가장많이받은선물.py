'''
Author    : semi
Date      : 2025.07.26(Sat)
Runtime   : ms
Memory    : KB
Algorithm :
'''

def get_gift_index(gift_status):
    n = len(gift_status)
    gift_index = []
    cols = list(zip(*gift_status))

    for i in range(n):
        given =sum(gift_status[i])
        # received =sum(cols[i])
        received = sum(gift_status[j][i] for j in range(n))
        gift_index.append(given-received)

    return gift_index

def get_gift_status(friends,gifts):
    n = len(friends)

    # i 행의 합 : i번 사람이 남에게 준 선물 수
    # i 열의 합 : i번 사람이 남에게 받은 선물 수
    gift_status = [[0]*n for _ in range(n)]

    #이름 -> 인덱스 매핑
    name_index = {name : idx for idx, name in enumerate(friends)}

    # 선물 현황 추가
    for record in gifts:
        #a :준사람  b:받은 사람
        giver,receiver = record.split()
        giver_idx = name_index[giver]
        receiver_idx = name_index[receiver]

        gift_status[giver_idx][receiver_idx] +=1

    return gift_status

def solution(friends,gifts):

    n = len(friends)
    result = [0] * n

    # 선물 현황 계산
    gift_status = get_gift_status(friends,gifts)
    
    # 선물 지수 계산
    gift_index = get_gift_index(gift_status)

    # 선물횟수 비교 -> 모든 사람 쌍을 비교해야한다.
    for i in range(n):
        for j in range(i+1,n):
            if gift_status[i][j]==gift_status[j][i]:
                if gift_index[i] > gift_index[j]:
                    result[i] +=1
                elif gift_index[i] < gift_index[j]:
                    result[j] +=1
            elif gift_status[i][j] > gift_status[j][i]:
                result[i] += 1
            else:
                result[j] +=1

    # print(result)
    return max(result)


friend = ["muzi", "ryan", "frodo", "neo"]
gift = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

solution(friend,gift)