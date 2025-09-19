'''
https://school.programmers.co.kr/learn/courses/30/lessons/84512
Author    : semi
Date      : 2025.09.17(Wed)
Algorithm : 구현
'''
def dfs(current_word,dict_word,ans):
    if(current_word==dict_word):
        return ans

    #base : 길이가 5가되면 종료한다.
    if len(current_word) == 5:
        return
    #recrusive : a~u까지 가지를 뻗는다.
    for i in range(1,6):
        ans +=1
        new_word = current_word + str(i)
        result = dfs(new_word,dict_word,ans) #반환값 받기

        if result is not None: #보고서에 내용이 있다면
            return result

def solution(word):
    vowls = {ch: idx for idx, ch in enumerate("AEIOU", start=1)}
    word_num = ""
    answer=0
    result = 0

    #단어 -> 숫자로 매칭
    for i in word:
        word_num += str(vowls[i])
    
    print(f"word_num = { word_num }")
    result = dfs("",word_num,answer)

    return result

print(solution("AE"))