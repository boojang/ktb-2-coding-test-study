'''
Author    : semi
Date      : 2025.11.17(Mon)
Runtime   : 300ms
Memory    : 36080KB
Algorithm :
'''
from collections import Counter
import sys

input = sys.stdin.readline

string = input().strip().upper()
str_count = Counter(string)

max_s = str_count.most_common(2)

# 1개밖에 없으면 그대로 출력
if len(max_s) == 1:
    print(max_s[0][0])
# 최댓값이 2개 이상이면 ?
elif max_s[0][1] == max_s[1][1]:
    print("?")
# 아니면 최댓값 1개
else:
    print(max_s[0][0])
