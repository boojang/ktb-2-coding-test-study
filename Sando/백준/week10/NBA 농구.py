# https://www.acmicpc.net/problem/17413

# * Author : Kang San Ah
# * Date : 2025.07.13(Sun)
# * Runtime : 1 sec
# * Memory : 128 MB
# * Algorithm : 
import sys
input = sys.stdin.readline

from datetime import timedelta

score = [0, 0] # 이기고 지는 쪽에 따라 시간 분배 위해 
time_lead = [timedelta(), timedelta()] # 정답 배열

time_prev = timedelta() # 첫 선언 시 0

# 입력
n = int(input()) # 3

# 입력
for i in range(n):
    team, time_str = input().split() # 1 01:10
    m, s = map(int, time_str.split(":")) # 01 , 10
    team  = int(team) - 1 # score 배열에 저장하기 위해. 0-indexed
    time_curr = timedelta(minutes = m, seconds = s) # 현재 시간
    
    # 현재까지 리드한 팀에게 시간 누적
    if score[0] > score[1]:
        time_lead[0] += time_curr - time_prev
    elif score[1] > score[0]:
        time_lead[1] += time_curr - time_prev
    
    score[team] += 1 
    time_prev = time_curr

# 경기 종료까지 리드한 팀 처리
time_end = timedelta(minutes= 48)
if score[0] > score[1]:
        time_lead[0] += time_end - time_prev
elif score[1] > score[0]:
        time_lead[1] += time_end - time_prev

# 출력
for tl in time_lead: 
    mm = str(tl.seconds // 60).zfill(2) # 2자리로 맞추기
    ss = str(tl.seconds % 60).zfill(2) 
    print(f"{mm}:{ss}")
    

