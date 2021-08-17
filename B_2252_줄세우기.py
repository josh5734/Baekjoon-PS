import sys
from collections import deque


def topological_sort(start):
    while q:
        curr = q.popleft()
        printResult.append(curr)
        for next in graph[curr]:
            indegree[next] -= 1
            outdegree[next] -= 1
            if indegree[next] == 0:  # 다음 정점의 indegree = 0이면 q에 삽입
                q.append(next)


printResult = []
if __name__ == "__main__":
    n, m = map(int, input().split())

    # 진입, 진출차수
    indegree, outdegree = [0] * (n+1), [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        pre, after = map(int, sys.stdin.readline().split())
        graph[pre].append(after)
        indegree[after] += 1
        outdegree[pre] += 1

    # indegree = 0인 정점에 대해 위상정렬 수행
    q = deque()
    for v in range(1, n+1):
        if indegree[v] == 0:
            q.append(v)

    topological_sort(q)

    # 결과 출력
    for p in printResult:
        print(p, end=' ')
