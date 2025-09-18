# https://school.programmers.co.kr/learn/courses/30/lessons/84512

# * Author : Kang San Ah
# * Date : 2025.09.17(Wed)
# * Algorithm : dfs

def solution(word):
    answer = []
    alpha = ['A', 'E', 'I', 'O', 'U']
    def dfs(word):
        if len(word) >5 :
            return
        if word : 
            answer.append(word)
        for ch in alpha: 
            dfs(word + ch)
    
    dfs('')
    return answer.index(word) + 1