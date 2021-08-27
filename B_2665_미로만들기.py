import sys, heapq

def bfs(x, y):
    visited = [[False] * n for _ in range(n)]   # 방문을 체크할 리스트
    pq = []
    heapq.heappush(pq, (0, x, y))
    while pq:
        count, curr_x, curr_y  = heapq.heappop(pq)
        
        # 끝에 도달하면 결과값 리턴
        if curr_x == n-1 and curr_y == n-1:
            return count

        for i in range(4):
            next_x, next_y = curr_x + dx[i], curr_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < n and not visited[next_x][next_y]:
                # 검은 방인 경우 흰 방으로 바꾼다.
                if graph[next_x][next_y] == 0:
                    heapq.heappush(pq,(count+1, next_x, next_y))
                else:
                    heapq.heappush(pq,(count, next_x, next_y))
                visited[next_x][next_y] = True
        

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

# 결과 출력하기
print(bfs(0,0))


