'''
Author    : semi
Date      : 2025.07.16(Wed)
Runtime   : 52ms
Memory    : 32412KB
Algorithm : 구현
'''


sc_1 = 0
time_1=0 #누적 시간
time_1_last = 0 #이기고 있던 최초시간
sc_2 = 0
time_2=0
time_2_last=0

n = int(input())

for i in range (n):
    a,b = input().split()
    mm,ss = b.split(':') # 분,초를 나누다.
    goal_time = int(mm)*60 + int(ss) #초로 변환해서 저장,계산에 용이

    if a == '1': #1팀이 골을 넣음
        sc_1 += 1

        if sc_1 > sc_2 and sc_1-1 == sc_2: # 최초 이기고 있었을 때 시간 기록
            time_1_last = goal_time

        elif sc_1 == sc_2 : #다시 동점 -> 2팀이 이기고 있는 구간 끝
            #이기고 있던 시간 누적
            time_2 += goal_time - time_2_last

    else: # 2팀이 골을 넣음
        sc_2 += 1

        if sc_2 > sc_1 and sc_2-1 == sc_1: # 최초 이기고 있었을 때
            time_2_last = goal_time

        elif sc_2 == sc_1: #다시 동점
            time_1 += goal_time - time_1_last



# 최종결과
end_time = 48*60

if sc_1 > sc_2: #1팀 우승
    # 48분 = 2880초
    time_1 += end_time - time_1_last
elif sc_1 < sc_2: #2팀 우승
    time_2 += end_time - time_2_last

# 출력
mm_1 = time_1 //60
ss_1 = time_1 % 60
print(f"{mm_1:02d}:{ss_1:02d}")
mm_2 = time_2 //60
ss_2 = time_2 % 60
print(f"{mm_2:02d}:{ss_2:02d}")