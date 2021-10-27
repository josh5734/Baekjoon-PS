import heapq as hq

import sys
input = sys.stdin.readline

def bfs(start_x, start_y, end_x, end_y, direction):
    visited = [[False] * w for _ in range(h)]
    q = []
    hq.heappush(q, (0, start_x, start_y, direction))
    visited[start_x][start_y] = True
    # 거울을 설치해야 하는 횟수
    while q:
        mirrors, curr_x, curr_y, curr_dir = hq.heappop(q)
        visited[curr_x][curr_y] = True
        if curr_x == end_x and curr_y == end_y:
            return mirrors

        for i in range(4):
            next_x, next_y = curr_x + dx[i], curr_y + dy[i]

            if 0 <= next_x < h and 0 <= next_y < w:
                if graph[next_x][next_y] != '*':
                    if not visited[next_x][next_y]:
                        
                        # 처음 시작점에서 나가는 경우
                        if curr_dir == -1:
                            hq.heappush(q,(mirrors, next_x, next_y, i))
                        else:
                            # 진행 방향이 다른 경우 거울 추가
                            if curr_dir != i:
                                hq.heappush(q,(mirrors+1, next_x, next_y, i))
                            else:
                                hq.heappush(q,(mirrors, next_x, next_y, i))
                                
w, h = map(int, input().split())
graph = [[] * w for _ in range(h)]

# 'C'가 위치한 두 좌표
dest = []

for i in range(h):
    line = list(input().rstrip())
    for j in range(w):
        if line[j] == 'C':
            dest.append((i,j))
        graph[i].append(line[j])
    
dx, dy = [1,-1,0,0], [0,0,1,-1]

# 거울을 설치한다 = 꺾이는 지점
start_x, start_y = dest[0][0], dest[0][1]
end_x, end_y = dest[1][0], dest[1][1]

# 시작점과 도착점의 좌표, 시작할 때 방향은 -1
print(bfs(start_x, start_y, end_x, end_y, -1))
