# https://school.programmers.co.kr/learn/courses/30/lessons/258712

# * Author : Kang San Ah
# * Date : 2025.07.24(Thu)
# * Runtime : 2 sec
# * Memory : 512 MB
# * Algorithm : BFS

from collections import Counter, defaultdict

def solution(friends, gifts):
    idx = {name: i for i, name in enumerate(friends)}
    give_cnt = defaultdict(int)
    gift_score = Counter()

    for gift in gifts:
        sender, receiver = gift.split()
        give_cnt[(sender, receiver)] += 1
        gift_score[sender] += 1
        gift_score[receiver] -= 1

    result = defaultdict(int)
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            a, b = friends[i], friends[j]
            a2b = give_cnt[(a, b)]
            b2a = give_cnt[(b, a)]

            if a2b > b2a:
                result[a] += 1
            elif a2b < b2a:
                result[b] += 1
            else:
                if gift_score[a] > gift_score[b]:
                    result[a] += 1
                elif gift_score[a] < gift_score[b]:
                    result[b] += 1

    return max(result.values(), default=0)


# 두 번째 코드 : 조금 더 간결한 코드 (100점)
# def solution(friends, gifts):
#     n = len(friends)
#     idx = {name: i for i, name in enumerate(friends)}
    
#     give = [[0] * n for _ in range(n)]
#     gift_score = [0] * n  # 준 - 받은
    
#     for gift in gifts:
#         sender, receiver = gift.split()
#         i, j = idx[sender], idx[receiver]
#         give[i][j] += 1
#         gift_score[i] += 1
#         gift_score[j] -= 1

#     result = [0] * n
    
#     for i in range(n):
#         for j in range(i+1, n):
#             if give[i][j] > give[j][i]:
#                 result[i] += 1
#             elif give[i][j] < give[j][i]:
#                 result[j] += 1
#             elif gift_score[i] > gift_score[j]:
#                 result[i] += 1
#             elif gift_score[i] < gift_score[j]:
#                 result[j] += 1
#             # 같으면 둘 다 아무것도 받지 않음
    
#     return max(result)


# 첫 번째 코드 : 논리적으로 ok, but 비효율적이라 실패 (30점)

# def solution(friends, gifts):
#     answer = 0
    
#     # 사람 별 인덱스 저장 딕셔너리
#     dc = {}
#     for idx, name in enumerate(friends) : 
#         dc[name] = idx # {('muzi' : 0)} ...
    
#     # 선물 주고 받은 2차원 배열
#     arr = [[0 for i in range(len(friends))]for j in range(len(friends))]
    
#     # 선물 지수 저장 배열
#     points = [[0 for i in range(3)]for j in range(len(friends))]
    
#     # 선물 저장 
#     for i in gifts:
#         sender, reciever = map(str, i.split())
#         arr[dc[sender]][dc[reciever]] += 1
#         points[dc[sender]][0] += 1 # 준 선물
#         points[dc[reciever]][1] += 1 # 받은 선물
    
#     # 선물 지수 계산
#     for i in range(len(friends)):
#         arr[i][i] = -1 # 자기 자신은 -1 처리
#         points[dc[friends[i]]][2] = points[dc[friends[i]]][0] - points[dc[friends[i]]][1] 
    
#     answer_arr = [0] * len(friends)
    
#     # 선물 받은 개수 구하기
#     for i in range(len(friends)-1):
#         for j in range(len(friends)):
#             if arr[i][j] != -1:
#                 if arr[i][j] > arr[j][i]:
#                     answer_arr[i] += 1
#                 elif arr[i][j] == arr[j][i] :
#                     if points[dc[friends[i]]][2] > points[dc[friends[j]]][2] : 
#                         answer_arr[i] += 1
#                     elif points[dc[friends[i]]][2] < points[dc[friends[j]]][2] :
#                         answer_arr[j] += 1
#                     else: 
#                         answer_arr[i], answer_arr[j] = 0,0
                    
#     answer = max(answer_arr)
    
#     return answer

