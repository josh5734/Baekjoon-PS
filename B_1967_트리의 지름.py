from collections import defaultdict, deque
import sys

def bfs(start):
    node, diameter = 0, 0

    visited = [False] * (n+1)
    visited[start] = True
    q = deque()
    q.append((start, 0))    

    while q:
        now, cost = q.popleft()

        if diameter < cost:
            diameter = cost
            node = now

        for t in tree[now]:
            child, weight = t[0], t[1]
            if not visited[child]:
                q.append((child, cost + weight))
                visited[child] = True
    return node, diameter



n = int(input())
tree = defaultdict(list)

# 트리 초기화
for _ in range(n-1):
    a, b, weight = map(int, sys.stdin.readline().split())
    tree[a].append((b, weight))
    tree[b].append((a, weight))
    

randomNode, maxDist = bfs(1)
randomNode, maxDist = bfs(randomNode)
print(maxDist)