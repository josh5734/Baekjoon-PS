import sys
def dfs(x, y, state):
    global count
    if x == n-1 and y == n-1:
        count += 1
    if state == "horizontal":
        # 가로 이동
        if y + 1 < n and graph[x][y + 1] == 0:
            dfs(x, y+1, "horizontal")
        # 오른쪽 대각선 이동
        if x + 1 < n and y+1 < n and graph[x+1][y] == 0 and graph[x+1][y+1] == 0 and graph[x][y+1] == 0:
            dfs(x+1,y+1,"diagonal")

    elif state == "vertical":
        # 세로 이동
        if x + 1 < n and graph[x+1][y] == 0:
            dfs(x+1,y,"vertical")

        # 오른쪽 대각선 이동
        if x + 1 < n and y+1 < n and graph[x+1][y] == 0 and graph[x+1][y+1] == 0 and graph[x][y+1] == 0:
            dfs(x+1,y+1,"diagonal")

    elif state == "diagonal":
        # 가로 이동
        if y + 1 < n and graph[x][y+1] == 0:
            dfs(x,y+1,"horizontal")
        # 세로 이동
        if x + 1 < n and graph[x+1][y] == 0:
            dfs(x+1,y,"vertical")
        # 대각선 이동
        if x + 1 < n and y + 1 < n and graph[x+1][y] == 0 and graph[x][y+1] == 0 and graph[x+1][y+1] == 0:
            dfs(x+1,y+1,"diagonal")
    
    return False

# dfs를 하면서 도착하면 count를 증가시킨다.
if __name__ == "__main__":
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
    count = 0
    state = "horizontal"
    dfs(0,1,state)
    print(count)