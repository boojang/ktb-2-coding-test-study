'''
Author    : semi
Date      : 2025.05.20(Tues)
Runtime   : 176ms
Memory    : 32412KB
Algorithm :
'''

n,m = map(int,input().split())


used = [False] * (n+1)

def backtracking(current_sequence):

    
    if len(current_sequence) == m:
        print(*current_sequence)
        return
    
    for i in range(1,n+1):
        
        if not used[i]:
            used[i] = True
            backtracking(current_sequence+[i]) # 새로운 리스트 만들기
            used[i] = False # 원상 복구
            

backtracking([])



'''
if m ==1:
    # 제너레이터 객체를 출력한다. -> 왜?
    # print(i for i in range(1,n+1))
    for i in range(1,n+1):
        print(i)
    print(*range(1,n+1))
else:
    #하나씩 기준을 정해서 backtracking에 넣는다.
    #★ Problem : 이미 backtracking 함수 안에서 기준을 잡고 돌고 있다.
    for i in range(1,n+1): # 기준이 되는 숫자
        # print(f"지금 기준 숫자:{i}")
        used[i] = True
        current = [i]
        backtracking(current)
        used[i] = False
'''

