'''
Author    : semi
Date      : 2025.05.20(Tues)
Runtime   : 164ms
Memory    : 32412KB
Algorithm :
'''

n,m = map(int,input().split())


used = [False] * (n+1)
sequence = []         
   
def backtracking():

    
    if len(sequence) == m:
        print(*sequence)
        return
    
    for i in range(1,n+1):
        
        if not used[i]:
            used[i] = True
            sequence.append(i)
            backtracking() # 새로운 리스트 만들기
            sequence.pop() # 원상 복구
            used[i] = False # 원상 복구

backtracking()