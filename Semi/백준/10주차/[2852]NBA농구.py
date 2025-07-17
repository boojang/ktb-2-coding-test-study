# 골이 들어간 시간/ 팀
# 48분 동안 진행
# 1번팀이 이기고 있던 time / 2번팀이 이기고 있던 time
# 0 : 0 아무도 이기고 있는거 아님
# b : mm:ss
# mm%10 >0 mm<=47 ss = [0,59]

# 이겼다 -> 상대 편 보다 score가 커야함
# 골을 넣음 -> 비교함 상대방보다 커
# -> (전체시간)-(골을 넣기전 시간) 까지 이기고 있는거
# 골을 넣었음 -> 상대방보다 큼 -> 그때 시간으로 업데이트
# 클 경우 : 사건이 일어났을 때 시간 - 골을 넣은 시간
# 만약 사건이 일어나지 않으면 끝난시간 -> 48

# 문제
# 이기고 있던 시간 계산을 어떻게 하지? -> mm*60+ss 형태로 변환
# 마지막으로 골을 넣은 타임을 알아야함 + 이기고 있는지 지고 있는지
# 숫자가 아니라 문자열인데 숫자 계산을 어떻게 하지?


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