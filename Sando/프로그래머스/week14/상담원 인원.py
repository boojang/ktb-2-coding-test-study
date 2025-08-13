# https://school.programmers.co.kr/learn/courses/30/lessons/214288

# * Author : Kang San Ah
# * Date : 2025.08.13(Wed)
# * Algorithm : greedy + simulation + pq + memoization

def solution(k, n, reqs):
    from collections import defaultdict
    import heapq

    d = defaultdict(list)
    
    # 그룹핑
    for r in reqs : 
        start, duration, typ = r[0], r[1], r[2]
        d[typ].append([start, duration])
    
    for typ in range(1, k + 1) : 
        d[typ].sort(key = lambda x : x[0])
    
    # 최소 시간을 반환
    def simulation(r, c): 
        waiting_time = 0
        pq = []
        # 초기화
        for _ in range(c) : 
            heapq.heappush(pq, 0) # min-heap
        
        # 요청 목록에 맞게 처리, 
        for start, duration in r :
            t = heapq.heappop(pq)
            if t <= start : # 상담원이 비어있다면
                heapq.heappush(pq, start + duration) # 종료시간을 저장
            else : 
                # 비어있지 않다면 대기시간 증가, 종료시간 갱신 
                waiting_time += (t- start)
                heapq.heappush(pq, t+duration)
        return waiting_time
    
    # w(t, c)는 type t에 상담원 c명을 배치했을 때 대기시간
    cache =  {}
    def w(t,c) :
        if (t,c) not in cache :
            cache[(t,c)] = simulation(d[t] , c) # 키는 튜플, 밸류는 simulate 값
        return cache[(t,c)]
    
    # 최소 유형 당 1명 씩 배치
    assign = [1] * (k+1) # 미리 한명 씩
    remain = n - k  # 각 유형에 한명 씩 배치 후 남은 수
    total_wait = sum(w(t,1) for t in range(1, k+1)) # 유형 별로 한명 씩 배치했을 때 대기시간의 총합
    
    # 남은 인원 배분 (그리디) 각 유형에 한명 씩 더 추가할 때 얼마나 줄어드는지 계산
    heap = []
    for t in range(1, k+ 1):
        gain = w(t,1) - w(t,2) if n >= 2 else 0
        heapq.heappush(heap, (-gain,t)) 
    
    while remain > 0 :
        neg_gain, t = heapq.heappop(heap)
        cur_c = assign[t]
        nxt_c = cur_c +1
        assign[t]  = nxt_c
        remain -=1
        
        # 총 대기 시간 갱신
        total_wait += w(t, nxt_c) - w(t, cur_c)
        
        if nxt_c + 1<= n:
            nxt_gain = w(t, nxt_c) - w(t, nxt_c + 1)
            heapq.heappush(heap, (-nxt_gain, t))
    
    return total_wait

print(solution(3,5, 	[[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]))