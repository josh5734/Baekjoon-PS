def dfs(x, y, visited, count, p):
    global answer
    if count == n:
        answer += p
        return
            
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not visited[nx][ny]:
            dfs(nx, ny, visited, count+1, p * prob[i])
            visited[nx][ny] = False
            
line = list(map(int, input().split()))
n, prob = line[0], list(map(lambda x : x / 100, line[1:]))
answer = 0
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0] # 동서남북

# 100*100 크기의 격자를 만들고 초기 위치를 (50, 50)으로 설정
visited = [[False] * (100) for _ in range(100)]
dfs(50, 50, visited, 0, 1)
print(answer)

