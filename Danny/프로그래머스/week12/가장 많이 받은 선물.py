def solution(friends, gifts):
    # 선물지수와 기록 저장용 딕셔너리
    gift_count = {name: {other: 0 for other in friends} for name in friends}
    gift_score = {name: 0 for name in friends}
    
    # 선물 주고받기 기록 채우기
    for g in gifts:
        giver, receiver = g.split()
        gift_count[giver][receiver] += 1
        gift_score[giver] += 1      # 준 횟수
        gift_score[receiver] -= 1   # 받은 횟수(마이너스)
    
    # 최종적으로 가장 많이 받은 사람 계산 (로직에 따라 다름)
    answer = max(gift_score.values())
    return answer

print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))