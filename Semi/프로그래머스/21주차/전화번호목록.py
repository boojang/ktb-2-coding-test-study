'''
https://school.programmers.co.kr/learn/courses/30/lessons/42577
Author    : semi
Date      : 2025.09.30(Tues)
Algorithm :
'''

def solution_hash(phone_book):
    prefix = {}
    for number in phone_book:
        prefix[number] = 1  # 전체 번호 자체를 먼저 dict에 넣음

    for number in phone_book:
        temp = ""
        for ch in number:
            temp += ch
            if temp in prefix and temp != number:  # 접두사 발견
                return False
    return True

def solution_sort(phone_book):
    answer=True
    phone_book.sort()

    #뒷 번호가 앞 번호를 포함하고 있는가?
    for i in range(len(phone_book)):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
            return answer

    return answer

'''
#problem : 번호의 "일부분"을 접두사로 생각했다. -> 문제 해석 오류
def solution(phone_book):
    answer = True
    prefix= {}
    for phone_number in phone_book:
        for i in range(2,len(phone_number)+1):
            part = phone_number[0:i]
            print(f"part = { part }")
            if part not in prefix:
                prefix[part] =1
                print(f"prefix = { prefix }")
            else:
                print("이미 존재")
                print(f"prefix = { prefix }")
                answer=False
                return answer

    return answer

'''