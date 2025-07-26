# 누가 선물을 많이 받을까?

# a,b -> 선물 많이 준 사람이 다음달 선물+1
# 기록x, 주고받은게 같음 -> 선물 지수가 더 큰 사람
# 선물지수 = 준 선물 - 받은 선물
# 선물지수도 같으면 선물 주고받기 x


# 어떻게 데이터를 저장하지?
# 친구 두 명씩 받은 선물 준 선물 비교 -> 다음달 받을 선물을 저장

# 문제점1
# get , rec로 받으면 누가 누구한테 얼마나 받은지 모름
# 이차원 배열을 만들어야함. + 각 인덱스가 누구를 뜻하는지 알아야함
# 문자열 -> 인덱스를 index()로? 계속 선형탐색 해야함. 비효율적
# 해결책1
# 딕셔너리로 미리 이름 -> 인덱스 맵을 만든다.


def get_gift_index(gift_status):
    n = len(gift_status)
    gift_index = []
    cols = list(zip(*gift_status))

    for i in range(n):
        given =sum(gift_status[i])
        received =sum(cols[i])
        received = sum(gift_status[j][i] for j in range(n))
        gift_index.append(given-received)

    return gift_index


def solution(friends,gifts):

    n = len(friends)
    result = [0] * n

    #이름 -> 인덱스 매핑
    name_index = {name : idx for idx, name in enumerate(friends)}

    # 선물현황 2차원 배열
    # gift_status = [[0] * len(friend)] * len(friend)
    gift_status = [[0]*n for _ in range(n)]

    # 선물 현황 추가
    for i in gifts:
        #a :준사람  b:받은 사람
        a,b = i.split()
        gift_status[name_index[a]][name_index[b]] +=1
        # print(f"a:{a}, name_index[a]: {name_index[a]} b:{b}, name_index[b]: {name_index[b]}")
        # print(gift_status)

    gift_index = get_gift_index(gift_status)
    # print(gift_index)

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