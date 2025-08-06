'''
Author    : semi
Date      : 2025.07.23(Wed)
Runtime   :
Memory    :
Algorithm : BFS
'''

# 직사각형 지도
# 각 칸 -> 그 지점의 높이
# 이동 -> 상하좌우만 가능 [1,0] [-1,0] [0,1] [0,-1]
# [0][0] -> [i][i]
# 내리막길로 이동 -> 위로 올라가지 않는다.

import sys

input = sys.stdin.readline()

M,N = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(M)]

move = [[1,0], [-1,0], [0,1], [0,-1]]