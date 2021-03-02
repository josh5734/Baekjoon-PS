from collections import deque
import sys
import copy
from itertools import combinations as C


def show(graph):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            print(graph[i][j], end=' ')
        print()


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < height and 0 <= ny < width:
                if testGraph[nx][ny] == 0:
                    testGraph[nx][ny] = 2
                    q.append((nx, ny))


if __name__ == "__main__":
    height, width = map(int, input().split())
    safetyZone = []
    graph = [[] for _ in range(height)]
    for i in range(height):
        graph[i] = list(map(int, sys.stdin.readline().split()))
    for i in range(height):
        for j in range(width):
            if graph[i][j] == 0:  # 추가로 벽을 세울 수 있는 곳
                safetyZone.append((i, j))

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    addWall = list(C(safetyZone, 3))  # 벽 3개를 세울 수 있는 모든 가능한 조합

    answer = []
    for wall in addWall:
        testGraph = copy.deepcopy(graph)
        for x, y in wall:  # 벽을 3개 세워본다.
            testGraph[x][y] = 1

        # bfs를 수행하면서 바이러스 전파
        for i in range(height):
            for j in range(width):
                if testGraph[i][j] == 2:
                    bfs(i, j)
        # 안전영역의 수 세기
        safety = 0
        for i in range(height):
            for j in range(width):
                if testGraph[i][j] == 0:
                    safety += 1
        answer.append(safety)

    print(max(answer))
