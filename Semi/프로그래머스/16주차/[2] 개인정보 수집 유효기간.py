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

    cal_pri = []
    answer = []

    #terms -> 어떻게 매칭시킬까? -> key, value로 구분
    #딕셔너리 -> ter_d[key값]으로 value를 알 수 있음
    ter_d = {k:int(v) for k,v in (term.split() for term in terms)}
    
    # 날짜 계산
    for privacy in privacies:
        date,term = privacy.split()

        year,month,day = date.split(".")
        month = int(month) + ter_d[term]

        if month >=13:
            year = int(year)+1
            #범위를 바꾸기
            month = (month-1)%12 +1

        day = int(day)-1
        # day = 0 일 경우
        if day == 0:
            month -= 1
            if month == 0:
                month = 12
            day = 28


        # new = ".".join(map(str,[year,month,day]))
        # new = "{}.{}.{}".format(year,month,day)
        new = f"{year}.{month}.{day}"
        print(f"new = {new}")

    # 유효기간 검증


    return answer


today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

solution(today,terms,privacies)