import sys
sys.setrecursionlimit(1000000)

# dfs를 수행하면서 대륙 번호를 구분
def dfs(x,y):
    global minLength
    # dfs를 돌기 전에 그 이전까지 구한 대륙들과 최소거리를 갱신
    for cont in continent[:continentNumber]:
        for ax,ay in cont:
            distance = abs(x-ax) + abs(y-ay) -1
            if distance < minLength:
                minLength = distance

    # 일반적인 dfs 수행 부분
    visited[x][y] = True
    continent[continentNumber].append([x,y])
    graph[x][y] = continentNumber
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx,ny)
    return True

if __name__ == "__main__":  # dfs를 다 돌고 난 뒤에 각 지점별 거리를 다시 처음부터 구하는 방식은 시간초과가 뜬다.
    n = int(input())
    # 대륙 정보 입력
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))

    dx, dy = [1,-1,0,0],[0,0,1,-1] 
    continent = [[] for _ in range(10000)]  # 대륙별 좌표를 가지는 리스트
    # dfs를 수행하면서 대륙 번호 매기기
    visited = [[False] * n for _ in range(n)]
    continentNumber = 1 # 대륙 번호
    minLength = 100000
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] == 1:
                if dfs(i,j) == True:
                    continentNumber += 1
    print(minLength)
