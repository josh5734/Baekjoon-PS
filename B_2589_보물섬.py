########## pypy3 ###############

import sys
from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))
    max_dist = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if tmap[nx][ny] == 'L' and distance[nx][ny] == 0:
                    q.append((nx, ny))
                    distance[nx][ny] = distance[x][y] + 1
                    if distance[nx][ny] >= max_dist:
                        max_dist = distance[nx][ny]
    return max_dist-1


if __name__ == "__main__":
    # 보물 지도의 세로, 가로 길이
    h, w = map(int, input().split())

    # 보물 지도 정보 입력받기
    tmap = []
    for i in range(h):
        tmap.append(input())

    # 이동 방향
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    max_distance = 0
    for i in range(h):
        for j in range(w):
            if tmap[i][j] == 'L':
                distance = [[0] * w for _ in range(h)]
                distance[i][j] = 1
                max_distance = max(max_distance, bfs(i, j))
    print(max_distance)
