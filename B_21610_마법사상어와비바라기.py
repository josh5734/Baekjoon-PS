import sys

# 그래프 크기와 명령 횟수
n, m = map(int, input().split())

# 그래프 입력받기 / 테두리를 0으로 입력
graph = [[0] * (n+2) for _ in range(n+2)]
waters = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for i in range(1, n+1):
    for j in range(1, n+1):
        graph[i][j] = waters[i-1][j-1]
winds = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
# 초기 구름 위치
cloud = [[n,1],[n,2],[n-1,1],[n-1,2]]

# 바람의 방향 / 1부터 8까지로 표현
dr, dc = [0, 0,-1,-1,-1,0,1,1,1], [0, -1,-1,0,1,1,1,0,-1]

# m번의 명령어만큼 반복
for i in range(m):
    d, s = winds[i]
    next_cloud = []

    # 비가 내렸던 구름인지 확인
    visited = [[False] * (n+1) for _ in range(n+1)]
    
    # 구름이 d 방향으로 s만큼 이동
    for r,c in cloud:
        nr = (r + s * dr[d]) % n
        if nr == 0: nr = n
        nc = (c + s * dc[d]) % n
        if nc == 0:nc = n
        graph[nr][nc] += 1
        next_cloud.append([nr,nc])
        visited[nr][nc] = True

    cloud = []

    # 대각선에 물이 있는 바구니 수만큼 물의 양이 증가
    for r,c in next_cloud:
        count = 0
        for i in [2,4,6,8]:
            nr, nc = r + dr[i], c + dc[i]
            if 1 <= nr <= n and 1 <= nc <= n and graph[nr][nc] > 0:
                count += 1
        graph[r][c] += count

    for r in range(1,n+1):
        for c in range(1,n+1):
            if graph[c][r] >= 2 and not visited[c][r]:
                cloud.append([c,r])
                graph[c][r] -= 2
    
answer = 0
for i in range(1, n+1):
    answer += sum(graph[i][1:n+1])
print(answer)