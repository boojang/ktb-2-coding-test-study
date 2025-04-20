'''
Author    : semi
Date      : 2025.04.20(Sun)
Runtime   : 468ms
Memory    : 34456KB
Algorithm : 
'''

n,m,k = map(int,input().split())
fire = []
cells = dict()

for i in range(m):
    r, c, m, s, d = map(int, input().split())
    fire.append((r - 1, c - 1, m, s, d))  # (행, 열, 질량, 속력, 방향) - 0-based 인덱스로 변환

dr =[-1,-1,0,1,1,1,0,-1]
dc =[0,1,1,1,0,-1,-1,-1]


for i in range(k):
    cells = dict() # 매 이동 명령마다 cells 초기화
    for fireball in fire:
        r,c,m,s,d = fireball #튜플 언패킹

        nr = (r + dr[d] * s) % n
        nc = (c + dc[d] * s) % n
        # print(f'nr:{nr}, nc:{nc}')

        cells.setdefault((nr,nc),[]).append((m,s,d))

        # print(cells)

    fire =[]

    for pos,fireballs in cells.items():
        r,c = pos # 0-based 좌표
        if(len(fireballs)==1):
            m,s,d = fireballs[0]
            fire.append((r,c,m,s,d)) # 다음 계산을 위해 0-based 좌표 그대로 사용
        else:
            total_m = sum(m for m,_,_ in fireballs)
            total_s = sum(s for _,s,_ in fireballs)
            count = len(fireballs)

            new_m = total_m//5
            if new_m == 0:
                continue

            new_s = total_s//count

            parities = [d % 2 for _,_,d in fireballs]

            if all(p == parities[0] for p in parities):
                new_d =[0,2,4,6]
            else :
                new_d = [1,3,5,7]

            for d in new_d:
                fire.append((r,c,new_m,new_s,d))
            # print(fire)
print(sum(m for _,_,m,_,_ in fire))