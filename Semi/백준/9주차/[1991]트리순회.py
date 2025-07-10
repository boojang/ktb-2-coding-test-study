'''
Author    : semi
Date      : 2025.07.10(Thur)
Runtime   : 32ms
Memory    : 32412KB
Algorithm : -
'''

#이진트리 입력 전위,중위, 후위
def preorder(node,result):
    if node == '.':
        return
    result.append(node)

    left, right = tree[node]
    preorder(left,result)
    preorder(right,result)

def inorder(node,result):
    if node == '.':
        return

    left,right = tree[node]
    inorder(left,result)
    result.append(node)
    inorder(right,result)

def postorder(node,result):
    if node == '.':
        return

    left,right = tree[node]
    postorder(left,result)
    postorder(right,result)
    result.append(node)

# 트리 데이터
tree = {}

# 노드의 개수
n = int(input())

# 결과물 저장
pre_result = []
in_result = []
post_result = []

# 노드 왼자식 오자식 -> 근데 숫자가 아니라 문자열로 온다. 어떻게 인접리스트에 넣을까?
# 인접리스트 -> 연결되어있는애들을 다 알 수 있다.
for _ in range(n):
    a,b,c = input().split()
    tree[a] = (b,c)

preorder('A',pre_result)
inorder('A',in_result)
postorder('A',post_result)

print("".join(pre_result))
print("".join(in_result))
print("".join(post_result))