import sys

# 트리 정점의 개수 n 
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child = map(int, sys.stdin.readline().split())
    tree[parent].append(child)   
    tree[child].append(parent)   

# 주어지는 질의의 개수
q = int(input())
for _ in range(q):
    op, cut = map(int, sys.stdin.readline().split())
    
    # 간선을 자르면 무조건 subtree로 나뉨
    if op == 2: print("yes")
    else:
        # 연결된 노드가 2개보다 적으면 sub tree X
        if len(tree[cut]) < 2 :
            print("no")
        else:
            print("yes")
            