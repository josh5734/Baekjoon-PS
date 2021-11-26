import sys
input = sys.stdin.readline

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
n, m, k = map(int, input().split())

# 땅의 정보, 나무 정보, 양분 정보
graph = [[5] * (n+1) for _ in range(n+1)]
tree = [[[] for _ in range(n+1)] for _ in range(n+1)]
feed = [[0] * (n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

for i in range(1, m+1):
    x, y, z = map(int, input().split())
    tree[x][y].append(z)

for _ in range(k):
    spread = []
    dead = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if tree[i][j]: # 나무가 존재하는 경우에 대해
                tree[i][j].sort() # 적은 양분을 가지고 있는 나무 우선
                temp = []
                for age in tree[i][j]:
                    if age <= graph[i][j]:
                        graph[i][j] -= age
                        age += 1
                        temp.append(age)
                        if age % 5 == 0: # 번식할 나무 목록에 추가
                            spread.append((i,j))
                    else: # 죽은 나무에 추가
                        dead.append((i,j,age // 2))
                tree[i][j] = temp

    for i, j, age in dead: # 죽은 나무는 양분이 된다.
        graph[i][j] += age

    for i, j in spread: # 나무 주변으로 번식한다.
        for k in range(8):
            nx, ny = i + dx[k], j + dy[k]  
            if 1 <= nx <= n and 1 <= ny <= n:
                tree[nx][ny].append(1)

    for i in range(1, n+1): # 땅에 양분을 공급한다.
        for j in range(1, n+1):
            graph[i][j] += feed[i][j]

answer = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        answer += len(tree[i][j])
print(answer)