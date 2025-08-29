def solution(n, w, num):
    # 전체 층 개수
    H = (n + w - 1) // w

    # num의 층(r)과 층 안에서 위치(p)
    r = (num - 1) // w + 1
    p = (num - 1) % w + 1

    # num의 열(c) 구하기
    if r % 2 == 1:  # 홀수층
        c = p
    else:           # 짝수층
        c = w - p + 1

    # "마지막 층 길이" 계산 함수
    def row_len(t):
        if t < H:
            return w
        else:
            return n - w * (H - 1) or w

    # 자기 자신 포함
    answer = 1

    # 위층 확인
    for t in range(r + 1, H + 1):
        lt = row_len(t)
        if t % 2 == 1:  # 홀수층
            if c <= lt:
                answer += 1
        else:           # 짝수층
            if c >= w - lt + 1:
                answer += 1

    return answer
