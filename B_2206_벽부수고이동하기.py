import sys
from collections import deque

sys.setrecursionlimit(10000)


def bfs(x, y):
    q = deque()
    q.append((x, y))
    arrive = False
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 이동 가능한 공간을 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

        if x == n-1 and y == m-1:
            arrive = True
    if not arrive:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                k = bfs2(nx, ny, graph[x][y]+1)
        return k
        # print(graph)
    return graph[n-1][m-1]


def bfs2(x, y, now):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 이동 가능한 공간을 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 1:

                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
        # print(graph)
    return graph[n-1][m-1] + now


if __name__ == "__main__":
    n, m = map(int, input().split())

    # graph 정보
    graph = [[] for _ in range(n)]
    for i in range(n):
        graph[i] = list(map(int, sys.stdin.readline().rstrip()))

    # 편의를 위해 graph의 0, 1 정보를 바꿔서 생각하자.
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
            else:
                graph[i][j] = 0

    # 이동할 수 있는 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    sp = bfs(0, 0)
    # 도착할 수 있다면 그 최단 경로는 항상 n+m-1보다는 크거나 같아야 함
    if sp < n+m-1:
        print(-1)
    else:
        print(sp)
