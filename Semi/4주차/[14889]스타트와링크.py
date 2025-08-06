'''
Author    : semi
Date      : 2025.05.20(Wed)
Runtime   : 2424ms
Memory    : 32412KB
Algorithm :
'''
from itertools import combinations

s = []
s_min=float('inf')

n = int(input())

# 입력값 받기
# s = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    # Prob team.append(map(int,input().split()))
    s.append(list(map(int,input().split())))
    
# 능력치 계산
def add_s(team):
    score =0
    for i in range(len(team)):
        for j in range(i+1,len(team)):
            a = team[i]
            b = team[j]
            score += s[a][b] + s[b][a]
        
    return score

# 팀 조합 + 능력치 계산
for team_a in combinations(range(n),n//2):
    team_b = list(set(range(n))-set(team_a))

    # team_a 계산
    s_a= add_s(team_a)
    # team_b 계산
    s_b= add_s(team_b)
    # 빼고 min이랑 비교하고 더하기
    s_min = min(s_min,abs(s_a-s_b))
    # print(f"s_a-s_b= {abs(s_a-s_b)}")
    # print(f"team_a:{team_a}, team_b:{team_b}")

print(s_min)

