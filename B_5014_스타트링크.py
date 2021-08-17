from collections import deque
# 건물 높이(F), 현재 위치(S), 목표 높이(G), 위 방향(U), 아래 방향(D)
F,S,G,U,D = map(int, input().split())
direction = [U,-D]

# 현재 위치에서 방문하지 않은 위 아래 방향을 탐색
visited = [0] * (F+1)
visited[S] = 1

# bfs 방식으로 탐색
q = deque()
q.append(S)
while q:
    curr = q.popleft()
    for i in range(2):
        next_floor = curr + direction[i]
        if 1 <= next_floor <= F and visited[next_floor] == 0:
            visited[next_floor] = visited[curr] + 1
            q.append(next_floor)
if visited[G] == 0:
    print("use the stairs")
else:
    print(visited[G]-1)