'''
Author    : semi
Date      : 2025.09.03(Wed)
Runtime   : ms
Memory    : KB
Algorithm :
'''

def solution(alp, cop, problems):

    #problem [alp_req, cop_req, alp_rwd, cop_rwd, cost]
    alp_max = max(row[0] for row in problems)
    cop_max = max(row[1] for row in problems)

    #조건 추가
    if alp>=alp_max and cop>=cop_max:
        return 0
    
    #조건 추가 : alp_max보다 alp가 더 큰 경우
    alp_max = max(alp_max,alp)
    cop_max = max(cop_max,cop)

    INF = float('inf')
    
    dp = [[INF]*(cop_max+1) for _ in range(alp_max+1)]
    print(f"dp = { dp }")

    dp[alp][cop] =0

    for i in range(alp,alp_max+1):
        for j in range(cop,cop_max+1):
            print(f"i,j = { i,j }")
            # 알고리즘 공부를 할 경우
            if i+1 <= alp_max:
                dp[i+1][j] = min(dp[i+1][j],dp[i][j]+1) #둘중 최단시간 저장
                print(f"알고리즘 공부: i,j,dp[i+1][j] = {i, j, dp[i + 1][j]}")
            if j+1 <= cop_max:
                dp[i][j+1] = min(dp[i][j+1],dp[i][j]+1)
                print(f"코딩 공부: i,j,dp[i][j+1] = {i, j, dp[i][j + 1]}")

            #문제 풀기
            for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
                if i >= alp_req and j >= cop_req: #문제를 풀 수 있는 상태

                    new_alp = min(alp_max,i+alp_rwd)
                    new_cop = min(cop_max,j+cop_rwd)
                    print(f"new_alp,new_cop = { new_alp,new_cop }")

                    # 새로운 경로
                    dp[new_alp][new_cop]= min(dp[new_alp][new_cop],dp[i][j]+cost)
                    print(f"문제풀기 : new_alp,new_cop,dp[new_alp][new_cop] = { new_alp,new_cop,dp[new_alp][new_cop] }")

    return dp[alp_max][cop_max]

alp=10
cop=10
problems = 	[[10,15,2,1,2],[20,20,3,3,4]]

solution(alp, cop, problems)

# 초기 설정 알고력i, 코딩력j을 만드는데 걸리는 시간
'''
    dp = [[i+j for j in range(cop_max)] for i in range(alp_max)]

    while alp < alp_max and cop < cop_max:
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            print(f"alp,cop = { alp,cop }")
            if alp < alp_req and cop < cop_req:  # 풀 조건
                continue
            if dp[alp][cop] + cost < dp[alp + alp_rwd][cop + cop_rwd]:  # 풀었을 때 더 시간이 적게 걸리는지 확인
                dp[alp + alp_rwd][cop + cop_rwd] = dp[alp][cop] + cost  # 값 변경
                alp += alp_rwd
                cop += cop_rwd
'''