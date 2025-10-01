'''
https://school.programmers.co.kr/learn/courses/30/lessons/84512
Author    : semi
Date      : 2025.09.17(Wed)
Algorithm : 구현
'''
def solution(word):
    dict = []
    vowels = "AEIOU"

    def dfs(current_word):
        dict.append(current_word)

        if len(current_word) == 5:
            return

        for v in vowels:
            dfs(current_word+v)


    dfs("")
    return dict.index(word)