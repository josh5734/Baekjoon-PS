from collections import defaultdict
import sys
input = sys.stdin.readline


def dfs(start, currNode, visited):
    visited[currNode] = True
    for nextNode in graph[currNode]:
        if not visited[nextNode]:
            height[start].add(nextNode)
            height[nextNode].add(start)
            dfs(start, nextNode,visited)


# 각 학생별로 자신보다 키가 큰 사람, 작은 사람을 저장하는 딕셔너리
height = defaultdict(set)
answer = 0
n, m = map(int, input().split())

# 키가 큰 사람에서 작은 방향으로 향하는 간선 그래프
graph = [[] for _ in range(n+1)] 
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 자신을 시작점으로 깊이 우선 탐색
# 시작점에서 출발하면서 거친 모든 노드는 시작점보다 키가 작다.
for i in range(1, n+1):
    visited = [False] * (n+1)
    dfs(i, i, visited)

# 자신보다 키가 큰 사람 + 작은 사람의 정보가 N-1명이면 가능
for i in range(1, n+1):
    if len(height[i]) == n-1:
        answer += 1
print(answer)