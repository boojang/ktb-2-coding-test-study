# https://www.acmicpc.net/problem/17413

# * Author : Kang San Ah
# * Date : 2025.07.11(Fri)
# * Runtime : 1 sec
# * Memory : 512 MB
# * Algorithm : String Processing

import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    result = []
    i = 0
    
    while i < len(s):
        if s[i] == '<':
            # 태그 처리: '<'부터 '>'까지 그대로 출력
            while i < len(s) and s[i] != '>':
                result.append(s[i])
                i += 1
            if i < len(s):  # '>' 추가
                result.append(s[i])
                i += 1
        elif s[i] == ' ':
            # 공백은 그대로 출력
            result.append(s[i])
            i += 1
        else:
            # 단어 처리: 공백이나 '<'가 나올 때까지 수집 후 뒤집기
            word = []
            while i < len(s) and s[i] != ' ' and s[i] != '<':
                word.append(s[i])
                i += 1
            # 단어를 뒤집어서 결과에 추가
            result.extend(reversed(word))
    
    return ''.join(result)

print(solve())