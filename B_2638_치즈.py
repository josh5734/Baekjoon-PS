import sys
from collections import deque


def checkOutsizeCheeze(i,j):
    visited = [[False] * m for _ in range(n)]
    visited[i][j] = True
    cheeze[i][j] = 2
    q = deque()
    q.append((i,j))

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and cheeze[nx][ny] != 1:
                visited[nx][ny] = True
                cheeze[nx][ny] = 2
                q.append((nx,ny))
    return False

def deleteCheeze():
    n, m = len(cheeze), len(cheeze[0])
    visited = [[False] * m for _ in range(n)]
    delete_list = []

    for i in range(1, n-1):
        for j in range(1, m-1):
            visited[i][j] = True
            count = 0
            for k in range(4):
                ni, nj = i + dx[k], j + dy [k]
                if cheeze[ni][nj] == 2:
                    count += 1
                    if count == 2:
                        delete_list.append((i,j))
                        break

    for x, y in delete_list:
        cheeze[x][y] = 0

n, m = map(int, input().split())
cheeze = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx, dy = [1,-1,0,0], [0,0,1,-1]
time = 0
while True:
    # 맨 바깥쪽 공기에서 dfs로 연결된 모든 치즈는 외부 치즈다.
    checkOutsizeCheeze(0,0)

    # 치즈 삭제
    deleteCheeze()
    time += 1
    
    # 모든 치즈가 녹았는지 확인
    cheezeCount = 0
    for i in range(n):
        for j in range(m):
            if cheeze[i][j] == 1:
                cheezeCount+= 1
    if cheezeCount == 0:
        break


print(time)