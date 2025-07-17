# https://www.acmicpc.net/problem/17413

# * Author : Kang San Ah
# * Date : 2025.07.11(Fri)
# * Runtime : 1 sec
# * Memory : 512 MB
# * Algorithm : String Processing

import sys
input = sys.stdin.readline

def solution():
    s = input()
    result = []
    i = 0
    
    while i < len(s):
        if s[i] == '<':
            while i < len(s) and s[i] != '>':
                result.append(s[i])
                i += 1
            if i < len(s):
                result.append(s[i])
                i += 1
        elif s[i] == ' ':
            result.append(s[i])
            i += 1
        else:
            word = []
            while i < len(s) and s[i] != ' ' and s[i] != '<':
                word.append(s[i])
                i += 1
            result.extend(reversed(word))
    
    return ''.join(result)

print(solution())
