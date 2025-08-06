'''
Author    : semi
Date      : 2025.07.30(Wed)
Runtime   : ms
Memory    : KB
Algorithm :
'''

# 1~n card + coin

# 각 라운드 마다 card +2
# card가 없다면 게임 종료
# card를 가질 때 동전 소모
# card 두장의 합 = n+1
# 낼 수 없다면 게임 종료

# 카드럴 먹냐 안먹냐에 따라서 카드

# 출력 : 게임에서 도달 가능한 최대 라운드 수

def solution(coin, cards):
    n = len(cards)
    my_card = []
    round = 1

    # 카드 가져가기
    my_card = cards[:n//3]
    cards = [n//3:]
    print(my_card)

    # 카드가 없으면 게임 종료
    while (len(cards) != 0):


    return round


coin = 4
cards = [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]

solution(coin,cards)
