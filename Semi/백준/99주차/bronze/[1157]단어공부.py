'''
Author    : semi
Date      : 2025.11.17(Mon)
Runtime   : 300ms
Memory    : 36080KB
Algorithm :
'''
from collections import defaultdict,Counter
import sys


input = sys.stdin.readline


string = input().strip()
str_dict = defaultdict(int)


for s in string:
    s=s.upper()
    str_dict[s] +=1

#최대값 - 동일하면 ?로 출력
max_s = max(str_dict.values())
max_list = [key for key,value in str_dict.items() if value==max_s]


if len(max_list)>1:
    print("?")
else:
    print(*max_list)