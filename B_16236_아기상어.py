import sys
from collections import deque

# bfs 탐색으로 먹을 수 있는 물고기들까지 거리를 구한다.
def getSmallerFishes(start_x,start_y,size):
    distance = [[0] * n for _ in range(n)]
    q = deque()
    visited = [[False]*n for _ in range(n)]
    q.append((start_x,start_y))
    visited[start_x][start_y] = True
    
    # 먹을 수 있는 물고기를 담는 리스트
    eatable = []
    while q:
        curr_x, curr_y = q.popleft()
        for i in range(4):
            next_x, next_y = curr_x + dx[i], curr_y + dy[i]
            # 공간 안에 있고 아직 방문하지 않은 물고기에 대해 탐색
            if  0 <= next_x < n and 0 <= next_y < n and not visited[next_x][next_y]:
                # 자신보다 사이즈가 작거나 같은 물고기는 지나갈 수 있음
                if graph[next_x][next_y] <= size:
                    q.append((next_x,next_y))
                    visited[next_x][next_y] = True
                    distance[next_x][next_y] = distance[curr_x][curr_y] + 1
                    if graph[next_x][next_y] < size and graph[next_x][next_y] != 0:
                        eatable.append((next_x,next_y, distance[next_x][next_y]))

    # 거리가 가까운 순, 가장 위쪽에 있는 순, 가장 왼쪽에 있는 순
    # pop할때 시간복잡도 고려하기 위해 역순 정렬
    return sorted(eatable, key= lambda x : (-x[2], -x[0], -x[1]))

# 공간의 크기 n
n = int(input())
answer = 0 

# 공간에 존재하는 물고기의 정보와 아기 상어 위치 얻기
graph = [[0] * n for _ in range(n)]
start_x, start_y, size = 0, 0, 2 # 최초 물고기 사이즈 = 2
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        graph[i][j] = row[j]
        if row[j] == 9:
            start_x, start_y = i,j

# 먹을 수 있는 물고기의 위치 정보 얻기
dx, dy = [1,-1,0,0],[0,0,1,-1]

# 엄마 상어가 필요할 때 까지 반복
count = 0
while True:
    fishToEat = getSmallerFishes(start_x,start_y,size)
    if len(fishToEat) == 0: break
    nx, ny, dist = fishToEat.pop()
    answer += dist # 이동 거리 더하기
    graph[start_x][start_y], graph[nx][ny] = 0, 0
    start_x, start_y = nx, ny # 물고기 위치 변화
    count += 1
    if count == size: # 사이즈와 같은 수만큼 물고기를 먹으면 사이즈 증가
        size += 1
        count = 0
print(answer)
