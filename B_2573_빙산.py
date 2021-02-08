############### PYPY3 #################

import sys
from collections import deque
sys.setrecursionlimit(100000)


def bfs(x, y, melted):
    visited = [[False] * m for _ in range(n)]
    count = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and melted[nx][ny] != 0:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1
    return count
# 빙하가 녹는 함수


def melt(n, m, ice, year, ice_number):
    # 1년이 지난 후 새로운 ice 정보
    melted = [[0] * m for _ in range(n)]
    x, y = 0, 0
    for i in range(n):
        for j in range(m):
            if ice[i][j] != 0:
                temp = 0
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if 0 <= nx < n and 0 <= ny < m:
                        if ice[nx][ny] == 0:
                            temp += 1
                # 빙산의 높이는 최소 0까지밖에 줄어들지 못함
                melted[i][j] = max(ice[i][j] - temp, 0)
                if melted[i][j] != 0:
                    x, y = i, j
                else:
                    ice_number -= 1
    year += 1
    if ice_number == 0:
        return 0
    if bfs(x, y, melted) != ice_number:
        return year

    return melt(n, m, melted, year, ice_number)


if __name__ == "__main__":
    # n, m 정보
    n, m = map(int, input().split())
    # 빙산 정보
    ice = []
    ice_number = 0
    start_x, start_y = 0, 0
    for i in range(n):
        line = list(map(int, sys.stdin.readline().split()))
        for j in range(m):
            if line[j] != 0:
                ice_number += 1
                # 처음 bfs를 확인해 볼 x, y 좌표 구하기
                start_x, start_y = i, j
        ice.append(line)

    # 주변을 확인하기 위한 방향 변수
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    year = 0
    # 처음에 2부분 이상으로 빙산이 나누어져 있는지 확인
    if bfs(start_x, start_y, ice) != ice_number:
        print(0)
    else:
        answer = melt(n, m, ice, year, ice_number)
        print(answer)
