import sys
from collections import deque


if __name__ == "__main__":
    # 토마토 상자의 크기
    m, n = map(int, input().split())

    # 토마토가 다 익기까지 걸리는 시간
    day = []
    not_visited = []

    q = deque()

    # graph 형태로 입력받기
    graph = [[] for _ in range(n)]
    for i in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        for j in range(m):
            graph[i].append(row[j])
            if row[j] == 1:
                q.append((i, j))
            elif row[j] == 0:
                not_visited.append((i, j))

    # 이동 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            # 이동하지 못하는 토마토
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
                day.append(graph[nx][ny])

    answer = 0
    flag = True
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                flag = False
            if graph[i][j] > answer:
                answer = graph[i][j]
    print(answer-1 if flag else -1)
