# https://school.programmers.co.kr/learn/courses/30/lessons/389478

# * Author : Kang San Ah
# * Date : 2025.08.25(Mon)
# * Algorithm : data structure

def solution(n: int, w: int, num: int) -> int:

    r = (num - 1) // w             
    p = (num - 1) % w              
    c = p if (r % 2 == 0) else (w - 1 - p)  

    full = n // w                   
    rem  = n %  w                   

    full_after = (full - 1 - r) if r < full else 0
    if full_after < 0:
        full_after = 0

    part = 0
    if rem > 0 and r < full:
        if full % 2 == 0:         
            part = 1 if c < rem else 0
        else:                        
            part = 1 if c >= w - rem else 0

    return 1 + full_after + part



n = 13
w = 3
num = 6
print(solution(n,w,num))