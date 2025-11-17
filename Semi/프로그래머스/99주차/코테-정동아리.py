
def solution_ex(students,n,m,k):
    club_name = {}; club_count = 0

    club_num = []
    club_majors = []

    for student in students:
        num,major,club = student.split()

        if club not in club_name:
            club_name[club] = club_count
            club_count +=1


'''
동아리별로 여러 학번/학과를 저장해야한다. -> 무슨 자료구조
하나의 key에 여러 value를 저장한다 -> list,set을 value로 쓰는 dict
'''
from collections import defaultdict,Counter

def solution(students,n,m,k):
    student_info = []
    student_num = Counter() #defaultdict(int)


    for s in students:
        num,major,club = s.split()
        student_info.append((num,major,club))
        student_num[num] +=1

    club_num = defaultdict(set)
    club_majors = defaultdict(set)
    club_years = defaultdict(set)

    for num,major,club in student_info:
        if student_num[num] >1:
            continue

        year = num[:2]
        club_num[club].add(num)
        club_majors[club].add(major)
        club_years[club].add(year)

        #조건에 맞는 동아리 세기
        count = 0

        for club in club_num:# club_num의 key가 들어감
            print(f"club = { club }")
            if len(club_num[club]) >=n and \
                len(club_majors[club]>=m) and \
                len(club_years[club])>=k:
                count+=1

        return count
