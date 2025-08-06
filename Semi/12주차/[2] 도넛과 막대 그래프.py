# 도넛 모양 그래프 -> n-1 정점 모두 방문 뒤 다시 정점으로
# 막대모양 그래프  -> n-1 정점 모두 한 번 씩 방문
# 팔자모양 그래프 2n+1 정점 2n+2 간선
from collections import defaultdict

def solution(edges):
    #1.나가는 간선과 들어오는 간선이 구분되어야 한다.
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    start = 0
    dounut,stick,eight = [0,0,0]

    # 3. start에서 인접한 정점을 시작으로 그래프를 확인해야해. == 각 그래프의 대표 노드
    adj = defaultdict(list)


    for o , i in edges:
        in_degree[i] +=1
        out_degree[o] +=1

    # 2. 생성한 정점 -> 근데 defaultdict로 하면 in_degree에 들어있지 않은데 어떡하지?
    nodes = set(in_degree) | set(out_degree)

    print(in_degree)
    print(out_degree)
    print(nodes)
    
    # 생성한 정점 찾기
    for node in nodes:
        if in_degree[node] ==0 and out_degree[node]>=2:
            start = node
            print(f"start = {start}")
    answer = []
    return answer

# 생성한 정점을 어떻게 알지? -> ★ in 0 out만 있다.
# 도넛 모양 in 1 out 1
# 막대 in 1 out 0
# 8자 모양 in 1 out 1 + 중간에 있는 친구 in 2 out 2

edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]

solution(edges)