import heapq
import sys

def bfs(x,y):
    visited = [[False] * m for _ in range(n)]

    q = []
    heapq.heappush(q,(0,x,y))
    visited[x][y] = True

    while q:
        count, curr_x, curr_y = heapq.heappop(q)
        if curr_x == n-1 and curr_y == m-1:
            return count
        for i in range(4):
            next_x, next_y = curr_x + dx[i], curr_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y]:
                visited[next_x][next_y] = True

                # 벽으로 막혀있는 경우                
                if graph[next_x][next_y] == 1:
                    heapq.heappush(q,(count+1, next_x, next_y))
                # 벽이 없을 때
                else:                    
                    heapq.heappush(q,(count, next_x, next_y))

m, n = map(int, input().split())
graph = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0,1,0,-1]
print(bfs(0,0))