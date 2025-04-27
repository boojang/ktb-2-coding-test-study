from collections import deque

t = int(input())
results = []

for _ in range(t):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))

    # (priority, is_target) 튜플을 deque에 저장
    queue = deque([(p, i == m) for i, p in enumerate(priorities)])
    count = 0

    while True:
        # 현재 큐에서 가장 큰 우선순위
        current_max = max(queue, key=lambda x: x[0])[0]
        # 큐의 맨 앞 문서를 확인
        front_priority, is_target = queue[0]

        if front_priority == current_max:
            # 해당 문서를 인쇄할 수 있음. 인쇄 카운트 증가 후 처리.
            count += 1
            queue.popleft()  # 문서 인쇄
            if is_target:  # 대상 문서라면 종료
                results.append(count)
                break
        else:
            # 큐의 맨 앞 문서의 우선순위가 최대가 아니므로 뒤로 이동
            queue.append(queue.popleft())

for res in results:
    print(res)
