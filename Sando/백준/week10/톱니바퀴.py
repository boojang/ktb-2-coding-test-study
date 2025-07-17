# https://www.acmicpc.net/problem/14891
# * Author : Kang San Ah
# * Date : 2025.07.14(Mon)
# * Runtime : 1 sec
# * Memory : 128 MB
# * Algorithm : Bit processing

import sys 
input = sys.stdin.readline


from sys import stdin
input = stdin.readline

# 톱니 상태 저장 (8비트)
gears = [int(input().strip(), 2) for _ in range(4)]

# 시계 방향 회전
def rotate_cw(g):
    last = g & 1            # 오른쪽 끝 비트
    g >>= 1
    if last:
        g |= (1 << 7)       # 왼쪽 끝에 1 추가
    return g

# 반시계 방향 회전
def rotate_ccw(g):
    first = (g >> 7) & 1    # 왼쪽 끝 비트 저장 -> 비트를 7번 오른쪽으로 밀겠다 -> 맨 왼쪽 비트가 맨 오른쪽으로 옴, 이 후 1인지 0인지 확인
    g = ((g << 1) & 0xFF)   # 왼쪽 shift 후 8비트 유지
    if first:               # 1이면
        g |= 1              # 오른쪽 끝에 왼쪽 끝 비트 추가
    return g

# 두 톱니의 맞닿은 극이 같은지 확인
def is_different(g1, g2):
    right = (g1 >> 2) & 1  # g1의 오른쪽 극 (2번 인덱스)
    left  = (g2 >> 6) & 1  # g2의 왼쪽 극 (6번 인덱스)
    return right != left

# 회전 명령 처리
def turn(idx, dir):
    directions = [0] * 4
    directions[idx] = dir

    # 왼쪽 방향 전파
    for i in range(idx - 1, -1, -1):
        if is_different(gears[i], gears[i+1]):
            directions[i] = -directions[i+1]
        else:
            break

    # 오른쪽 방향 전파
    for i in range(idx + 1, 4):
        if is_different(gears[i-1], gears[i]):
            directions[i] = -directions[i-1]
        else:
            break

    # 실제 회전 수행
    for i in range(4):
        if directions[i] == 1:
            gears[i] = rotate_cw(gears[i])
        elif directions[i] == -1:
            gears[i] = rotate_ccw(gears[i])

# 회전 명령 입력
k = int(input())
for _ in range(k):
    idx, d = map(int, input().split())
    turn(idx - 1, d)  # 톱니 번호는 0-based index로 조정

# 점수 계산 (12시 방향이 S극이면 2^i 점)
score = 0
for i in range(4):
    if (gears[i] >> 7) & 1:
        score += (1 << i)

print(score)



