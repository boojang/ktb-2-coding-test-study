#  * Author    : Kang San Ah
#  * Date      : 2025.07.03(Thu)
#  * Runtime   : 2 sec
#  * Memory    : 128 MB
#  * Algorithm : DFS

# 1991

import sys 
input = sys.stdin.readline

n = int(input())
tree = {} # 딕셔너리

for i in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

def preorder(node):
    if node == '.':
        return
    print(node, end ='')
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end ='')
    inorder(tree[node][1])

def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end ='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
