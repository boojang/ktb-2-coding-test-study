'''
https://school.programmers.co.kr/learn/courses/30/lessons/150370
Author    : semi
Date      : 2025.08.28(Thurs)
Algorithm :
'''

'''
개인정보 n
유효기간 month 1.5 -> 1.4까지
모든 달은 28일로 고정

1. 수집일자 + 약관 종류 유효기간
2. 현재를 넘으면 파기x -> 아니면 파기
return pri
'''



def solution(today, terms, privacies):

    answer = []

    #terms -> 어떻게 매칭시킬까? -> key, value로 구분
    #딕셔너리 -> ter_d[key값]으로 value를 알 수 있음
    ter_d = {k:int(v) for k,v in (term.split() for term in terms)}
    
    # 날짜 계산
    for idx,privacy in enumerate(privacies):
        date,term = privacy.split()

        year,month,day = date.split(".")

        # 일수로 통일 (28일을 안다)
        pri_day = int(year)*12*28 + int(month)*28 + int(day)
        term_day = ter_d[term]*28

        total_day = pri_day + term_day # 유효기간까지 날짜


        # 유효기간 검증
        year_t, month_t, day_t = today.split(".")
        today_day = int(year_t)*12*28 + int(month_t)*28 + int(day_t)
        
        if today_day >= total_day:
            #유효기간 마감
            answer.append(idx+1)

    return answer


today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

solution(today,terms,privacies)