from collections import deque
import sys
input = sys.stdin.readline

def isNotWall(sx, sy, w, h, dir):
    if dir == 0:
        boundary = [(i,sy) for i in range(sx, sx+h)]
    elif dir == 1:
        boundary = [(i, sy+w-1) for i in range(sx, sx+h)]
    elif dir == 2:
        boundary = [(sx, i) for i in range(sy, sy+w)]
    else:
        boundary = [(sx+h-1, i) for i in range(sy, sy+w)]
    for x, y in boundary:
        if graph[x][y] == 1:
            return False
    return True

def isInBoundary(x, y, w, h):
    if 0 <= x and x + h - 1 < n:
        if 0 <= y and y + w - 1 < m:
            return True
    return False

def bfs():
    visited = [[0] * m for _ in range(n)]

    # 왼쪽 상단 모서리만을 기준으로 생각한다.
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 0

    while q:
        currX, currY = q.popleft()
        if currX == ex and currY == ey:
            return visited[currX][currY]
        for i in range(4):
            nextX, nextY = currX + dx[i], currY + dy[i]
            if isInBoundary(nextX, nextY, w, h): # 범위 체크
                if not visited[nextX][nextY]: # 방문 체크
                    if isNotWall(nextX, nextY, w, h, i): # 벽 체크
                        visited[nextX][nextY] = visited[currX][currY] + 1
                        q.append((nextX, nextY))
    return -1

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
h, w, sx, sy, ex, ey = map(int, input().split())
sx, sy, ex, ey = sx-1, sy-1, ex-1, ey-1 # (0, 0)을 시작점으로 맞추기

dx, dy = [0,0,-1,1], [-1,1,0,0] # left, right, up, down
answer = bfs()
print(answer)

