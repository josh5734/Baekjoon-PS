import sys
from collections import deque

def bfs():
    # 이동할 수 있는 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    #visited[x][y][breakWall] = (x,y) 지점의 breakWall한 상태에서 거리
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1


    # 큐에 처음 거리 1과 시작점 (0,0), 벽을 부순 횟수(0)을 넣고 시작
    q = deque()
    q.append((0,0,0))
    result = []
    while q:
        x, y, breakWall = q.popleft()
  
        if x == n-1 and y == m-1:
            result.append(visited[x][y][breakWall])

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 이동할 위치가 벽인 경우 현재 벽을 한 번도 부수지 않았으면 벽을 부수고 이동    
                if graph[nx][ny] == 1:
                    if visited[nx][ny][1] == 0 and breakWall == 0:
                        visited[nx][ny][1] = visited[x][y][0] + 1
                        q.append((nx, ny, 1))
                # 벽이 아닌 경우
                else:
                    if visited[nx][ny][breakWall] == 0:
                        visited[nx][ny][breakWall] = visited[x][y][breakWall] + 1
                        q.append((nx, ny, breakWall))

    return min(result) if result else -1  


n, m = map(int, input().split())

# graph 정보
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().rstrip()))

print(bfs())