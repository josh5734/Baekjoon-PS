import sys
from collections import deque
import copy

sys.setrecursionlimit(100000)


def bfs(x, y, distance, fishes):
    global size, eat
    # 먹을 수 있는 물고기의 정보
    eatable = list(filter(lambda x: x[0] < size, fishes))
    if not eatable:
        return distance
    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((x, y))

    g = []
    for i in range(n):
        g.append([int(1e9)] * n)
    # 처음 아기 상어의 위치에 있는 값을 0으로 만든다.
    g[x][y] = 0

    candidate = []
    while q:
        x, y = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] <= size:
                if not visited[nx][ny]:
                    q.append((nx, ny))
                    g[nx][ny] = g[x][y] + 1

                    # 잡아 먹을 수 있다면
                    for fish in eatable:
                        if nx == fish[1] and ny == fish[2] and fish[3]:
                            candidate.append(fish)

    if candidate:
        f = sorted(candidate, key=lambda x: (g[x[1]][x[2]], x[1], x[2]))[0]
        nx, ny = f[1], f[2]
        eat += 1
        if eat == size:
            size += 1
            eat = 0
        distance += g[nx][ny]
        f[3] = False

        return bfs(nx, ny, distance, fishes)
    else:
        return distance


if __name__ == "__main__":
    n = int(input())

    loc, size = (), 2  # 처음 아기 상어의 위치, 사이즈

    fishes = []  # 물고기들의 정보

    graph = []
    for i in range(n):
        line = list(map(int, sys.stdin.readline().split()))
        for j in range(n):
            # 아기 상어의 위치
            if line[j] == 9:
                loc = (i, j)
            # 물고기들의 크기, 위치 정보
            elif line[j] != 0:
                fishes.append([line[j], i, j, True])
        graph.append(line)
    graph[loc[0]][loc[1]] = 0

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상어가 움직일 수 있는 방향
    eat = 0  # 최초 물고기를 잡아 먹은 횟수
    distance = 0  # 움직인 시간

    start_x, start_y = loc[0], loc[1]
    answer = bfs(start_x, start_y, distance, fishes)
    print(answer)
