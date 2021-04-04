import sys
sys.setrecursionlimit(100000)
def dfs(sx, sy):
    visited[sx][sy] = True
    for i in range(8):
        nx, ny = sx + dx[i], sy + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx,ny)
    return True 

if __name__ == "__main__":
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0: # 종료 조건
            break
        # 그래프 정보 입력
        graph = [[] for _ in range(h)]
        for i in range(h):
            graph[i] = list(map(int, sys.stdin.readline().split()))
            
        visited = [[False for _ in range(w)] for _ in range(h)]
        island = 0 # 섬의 개수
        dx, dy = [1,-1,0,0,1,-1,1,-1],[0,0,1,-1,1,1,-1,-1] # 가로, 세로, 대각선
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1 and not visited[i][j]:
                    if dfs(i,j) == True: # dfs 수행
                        island += 1
        print(island)
