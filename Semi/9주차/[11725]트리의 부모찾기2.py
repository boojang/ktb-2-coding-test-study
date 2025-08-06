from collections import deque
n = int(input())

#노드에 연결된 노드를 저장장
tree = [[]* for _ in range(n+1)]


for i in range(n-1):
    a,b = map(int(input().split()))
    tree[a].append(b)
    tree[b].append(a)
    

# 탐색을 할거에요. 루트노드 1 부터 시작해서 내려갈거에요
# 내려갈 노드를 저장할 queue -> 근데 왜 dequeue로 할까? -> '가장 가까운 노드' 부터 탐색을 해야하니까까
# BFS : 너비 우선탐색, 인접한/가까운 노드부터 탐색해야한다.
# 먼저 들어온 노드부터 탐색 -> 
# 내가 내려간 자국을 저장하는 parent 리스트
queue = deque(1)
parent= [0] * (n+1) #부모 노드를 저장 -> 출력

while queue:
    current = queue.popleft()
    # node : 인접한 노드
    for node in tree[current]:
        # 아직 부모노드가 정해지지 않았다면 -> parent가 0이라면면
        # current가 부모 노드가 되겠지?
        # 그리고 인접한 애들에 노드에도 접근해하니까
        # 그 아이들을 queue에 넣는다.
        if parent[node] == 0:
            parent[node] = current
            queue.append(node)
    