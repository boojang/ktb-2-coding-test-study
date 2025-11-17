
'''
1.일간 빙고 -> 1일마다
2. 주간 빙고 -> 목요일마다
3. 월간 빙고 -> 달이 바뀔때마다

12월 동안 유저가 몇 점 얻었는가?
(day,prob)
2022.12.1 목

day = [] 하루마다 업데이트 (1~9에 해당)
weekly = [] 1 8 15 22 29 마다 업데이트 (10~18)
monthly = [] 31에 업데이트 (19~27)

빙고를 맞춰야함 123 456 789  10 11

'''
#제출
def solution(logs):
    answer = 0
    prev_day = None

    day_marked = set()
    weekly_marked = set()
    monthly_marked = set()

    for log_day, num in logs:
        # 날짜 변경 시 초기화
        if log_day != prev_day:
            prev_day = log_day
            day_marked.clear()

            if log_day in [1, 8, 15, 22, 29]:
                weekly_marked.clear()
            if log_day == 31:
                monthly_marked.clear()

        # 각 빙고판에 번호 추가
        if 1 <= num <= 9:
            day_marked.add(num)
            answer += count_bingo(day_marked, start=1)

        elif 10 <= num <= 18:
            weekly_marked.add(num)
            answer += count_bingo(weekly_marked, start=10)

        elif 19 <= num <= 27:
            monthly_marked.add(num)
            answer += count_bingo(monthly_marked, start=19)

    return answer
def count_bingo(marked, start):
    """
    빙고 개수 전부 세기 (가로, 세로, 대각선)
    """
    bingo_count = 0

    # 가로줄 3개
    for r in range(3):
        row = {start + r*3, start + r*3 + 1, start + r*3 + 2}
        if row.issubset(marked):
            bingo_count += 1

    # 세로줄 3개
    for c in range(3):
        col = {start + c, start + 3 + c, start + 6 + c}
        if col.issubset(marked):
            bingo_count += 1

    # 대각선 2개
    if {start, start + 4, start + 8}.issubset(marked):
        bingo_count += 1
    if {start + 2, start + 4, start + 6}.issubset(marked):
        bingo_count += 1

    return bingo_count

#수정 - 빙고 중복 count 제거
def solution1(logs):
    answer = 0
    prev_day = None

    # 현재 선택된 칸
    day_marked = set()
    weekly_marked = set()
    monthly_marked = set()

    # 이미 완성된 줄
    day_done = set()
    weekly_done = set()
    monthly_done = set()

    for day, num in logs:
        # 날짜 변경 시 초기화
        if day != prev_day:
            prev_day = day
            day_marked.clear()
            day_done.clear()

            if day in [1, 8, 15, 22, 29]:
                weekly_marked.clear()
                weekly_done.clear()
            if day == 31:
                monthly_marked.clear()
                monthly_done.clear()

        # 각 영역에 기록
        if 1 <= num <= 9:
            answer += update_bingo(day_marked, day_done, num, 1)
        elif 10 <= num <= 18:
            answer += update_bingo(weekly_marked, weekly_done, num, 10)
        elif 19 <= num <= 27:
            answer += update_bingo(monthly_marked, monthly_done, num, 19)

    return answer
def update_bingo(marked, done, num, start):
    """
    num을 새로 선택했을 때,
    그로 인해 새로 완성된 빙고 줄 수만 반환
    """
    marked.add(num)
    bingo_lines = [
        {start, start+1, start+2},         # row1
        {start+3, start+4, start+5},       # row2
        {start+6, start+7, start+8},       # row3
        {start, start+3, start+6},         # col1
        {start+1, start+4, start+7},       # col2
        {start+2, start+5, start+8},       # col3
        {start, start+4, start+8},         # diag ↘
        {start+2, start+4, start+6}        # diag ↙
    ]

    new_score = 0
    for i, line in enumerate(bingo_lines):
        if i not in done and line.issubset(marked):
            done.add(i)
            new_score += 1
    return new_score


#다시 너가 만들어
def solution2(logs): #(1,1) (1,2) (1,3) (2,1)
    answer = 0
    today=1

    day_marked = set()
    weekly_marked = set()
    monthly_marked = set()

    day_scored = set() #이미 점수를 획득한것
    weekly_scored = set()
    monthy_scored = set()

    for day,num in logs:

        print(f"day,num = { (day,num) }")

        # -- 초기화 --
        if today != day: #날짜 달라지면 초기화
            day_marked.clear()
            today = day

        day_of_the_week = (3+(day-1)) %7 # 월 :0 ~ 일:6 오늘은 목요일 (3)
        if day_of_the_week == 3: #목요일이면 초기화
            weekly_marked.clear()

        # -- 빙고판 -- 점수를 체크하고 -> marked에 점수를 넣어야지+빙고를 확인해야함
        if num>=1 and num<=9:
            r,c= divmod(num-1,3) # (num-1)//3 , (num-1)%3
            day_marked.add((r,c))
            answer +=check_bingo(day_marked,day_scored)
            print(f"day : answer = { answer }")

        elif num>=10 and num<=18:
            #num -=9 #이러면 위랑 뭐가 달라?
            r,c= divmod(num-10,3) # (num-1)//3 , (num-1)%3
            weekly_marked.add((r,c))
            answer += check_bingo(weekly_marked, weekly_scored)
            print(f"weekly : answer = {answer}")
        else:
            r,c = divmod(num-19,3)
            monthly_marked.add((r,c))
            answer += check_bingo(monthly_marked,monthy_scored)
            print(f"monthly : answer = {answer}")

        print(f"total answer : {answer}")
def check_bingo(marked,already_score):
    #start를 어떻게 활용하지?
    #이미 점수 받은건 어떻게 저장하지? {((0,1),(1,1),(2,1))}
    #가로,세로,대각선 규칙이 set에 있는지 확인해야한다. 있으면 그건 day_score에 저장해야한다.
    # 그럼 반복문을 어떻게 돌리지?

    new_line = set() #합치기 위함

    #가로 -> 되는
    for r in range(3):
        line = tuple(sorted((r,c) for c in range(3))) #{((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2))}
        if set(line).issubset(marked) and line not in already_score:
            new_line.add(line)

    #세로
    for c in range(3):
        line = tuple(sorted((r,c) for r in range(3)))
        if set(line).issubset(marked) and line not in already_score:
            new_line.add(line)

    #대각선
    dig_line1 = tuple(((i,i) for i in range(3)))
    dig_line2 = tuple(((i,2-i) for i in range(3)))

    for line in (dig_line1,dig_line2):
        if set(line).issubset(marked) and line not in already_score:
            new_line.add(line)

    #점수 추가된 라인은 제외
    already_score |= new_line
    print(f"new_line = { new_line }")
    print(f"already_score = { already_score }")

    return len(new_line)#대박












logs = [
 [1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],
 [15,19],[15,10],[15,21],[15,9],[15,25],[15,1],[15,27],[15,13],
 [24,5],[24,16],[24,23]
]

logs2 = [[1,1],[1,2],[1,3],[1,14],[2,8],[2,22],[2,25],[8,19],]

print(solution2(logs))