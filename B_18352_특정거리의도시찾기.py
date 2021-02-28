from collections import deque
import sys


def bfs(distance, start, graph):
    visited = [False for _ in range(n+1)]
    count = 0
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        temp = []
        while q:
            now = q.popleft()
            for c in graph[now]:
                if not visited[c]:
                    temp.append(c)
                    visited[c] = True
        q.extend(temp)
        count += 1
        if count == k:  # 거리가 k이면 현재 위치를 return
            return temp
    return -1


if __name__ == "__main__":
    n, m, k, x = map(int, input().split())
    # 간선 정보 입력받기
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        sour, dest = map(int, sys.stdin.readline().split())
        graph[sour].append(dest)
    k_shortest = bfs(k, x, graph)
    if k_shortest == -1 or k_shortest == []:
        print(-1)
    else:
        for c in sorted(k_shortest):
            print(c)
