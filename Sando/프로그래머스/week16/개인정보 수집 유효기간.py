# https://school.programmers.co.kr/learn/courses/30/lessons/389479

# * Author : Kang San Ah
# * Date : 2025.08.25(Mon)
# * Algorithm : data structure
from collections import defaultdict
def solution(today, terms, privacies):
    answer = []

    d = defaultdict(int)
    for term in terms :
        typ = term.split(' ')[0]
        mon = term.split(' ')[1] 
        d[typ] = mon
        
    year = int(today.split('.')[0])
    month = int(today.split('.')[1]) 
    day = int(today.split('.')[2]) 
    
    for i, privacy in enumerate(privacies):
        date = privacy.split(' ')[0]
        type = int(d[privacy.split(' ')[1]]) * 28 
        
        num = (year - int(date.split('.')[0]))* 12 * 28 +(month - int(date.split('.')[1])) * 28 + (day - int(date.split('.')[2]))
        
        if num >= type : 
            answer.append(i+1)

    return answer


today = "2022.05.19"	
terms = ["A 6", "B 12", "C 3"]	
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]	
print(solution(today, terms, privacies))