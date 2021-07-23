from collections import defaultdict

def cutTreeByDFS(tree, isExistNode, node):
    isExistNode[node] = False
    for child in tree[node]:
        if isExistNode[child]:
            isExistNode[child] = False
            cutTreeByDFS(tree, isExistNode, child)

def dfs(tree, isExistNode, root):
    global count
    isExistNode[root] = False
    isLeafNode = True  
    for child in tree[root]:
        if isExistNode[child]:
            isLeafNode = False
            isExistNode[child] = False
            dfs(tree, isExistNode, child)
    if isLeafNode:
        count += 1

n = int(input()) # 노드의 개수
count = 0
tree = defaultdict(list)    # 자식 정보를 저장하는 트리
rootNode = -1
for childIndex, parent in enumerate(list(map(int, input().split()))):
    if(parent == -1):
        rootNode = childIndex
    else:
        tree[parent].append(childIndex) # 부모 노드의 번호 = 부모 노드가 해당 인덱스를 자식으로 갖는다.

deleteNode = int(input()) # 삭제할 노드의 번호
if rootNode == deleteNode: # 루트를 삭제하면 트리가 없어진다.
    print(0)
else:
    # deleteNode를 트리에서 cut - 이어진 자식 노드 삭제
    isExistNode = [True] * n
    cutTreeByDFS(tree, isExistNode, deleteNode)

    # leaf 노드의 개수 = dfs 탐색 경우의 수
    dfs(tree, isExistNode, rootNode)
    print(count)
