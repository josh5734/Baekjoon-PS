import sys
from collections import deque
def bfs(target):
    q = deque()
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    q.append((0,0))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    if abs(graph[nx][ny] - graph[x][y]) <= target:
                        if nx == n-1 and ny == n-1: return True
                        visited[nx][ny] = True
                        q.append((nx,ny))
    return False


input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
answer, lower, upper = 0, 0, 1000000000
while lower <= upper:
    mid = (lower + upper) // 2
    if bfs(mid):
        answer = mid
        upper = mid - 1
    else:
        lower = mid + 1
print(answer)

