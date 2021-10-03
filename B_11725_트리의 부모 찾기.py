from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 루트 노드부터 너비 우선 탐색
def findParent():
    visited = [False] * (n+1)
    visited[1] = True
    q = deque()
    q.append(1)
    while q:
        parent = q.popleft()
        for child in tree[parent]:
            if not visited[child]:
                parentNumber[child] = parent
                visited[child] = True
                q.append(child)


n = int(input())
tree = defaultdict(list)
for _ in range(n-1):
    a, b= map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 각 노드의 부모 번호를 저장하는 리스트
parentNumber = [-1] * (n+1)

# BFS를 통해 각 노드의 부모 노드 찾기
findParent()

# 결과 출력
for i in range(2, n+1):
    print(parentNumber[i])