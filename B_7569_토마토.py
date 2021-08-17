from collections import deque
import sys


def bfs(tomato_good):
    count = 0
    while tomato_good:
        z, x, y = tomato_good.popleft()
        for d in range(6):
            nz, nx, ny = z + dz[d], x + dx[d], y + dy[d]
            # 가능한 영역 체크
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    tomato_good.append((nz,nx,ny))
                    count += 1

    # 토마토를 다 익게 했으면 (마지막 익은 토마토의 값 - 1) 리턴
    if count == numOfBadTomato:
        return graph[z][x][y] - 1
    # 다 끝났을 때 아직 익지 못한 토마토가 있으면 -1 리턴
    else:
        return -1


answer = 0

# 가로, 세로, 높이
m, n, h = map(int, input().split())

graph = []
for _ in range(h):
    # 각 층에 존재하는 토마토 배열
    floor_graph = []
    for i in range(n):
        floor_graph.append(list(map(int, sys.stdin.readline().split())))
    graph.append(floor_graph)

dx, dy, dz = [0,0,1,-1,0,0], [0,0,0,0,1,-1], [1,-1,0,0,0,0] # 위, 아래, 동서남북


tomato_good = deque()
numOfBadTomato = 0
for i in range(h):
    for j in range(n):
        for k in range(m): 
            # 최초에 익은 토마토의 위치를 저장
            if graph[i][j][k] == 1:
                tomato_good.append((i,j,k))
                        
            # 익지 않은 토마토의 개수 세기
            if graph[i][j][k] == 0:
                numOfBadTomato += 1

# 처음에 다 익었으면 0 출력
if numOfBadTomato == 0:
    print(0)

# 토마토가 모두 익을 때까지 걸리는 시간 계산
else:
    print(bfs(tomato_good))