import sys
sys.setrecursionlimit(10000)


def dfs(start):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(node)


if __name__ == "__main__":
    # 노드, 간선 개수
    n, e = map(int, input().split())

    # 연결 요소의 개수
    cc = 0

    # 방문 기록을 체크하는 테이블
    visited = [False] * (n+1)

    # graph 정보
    graph = [[] for _ in range(n+1)]
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            cc += 1
    print(cc)
