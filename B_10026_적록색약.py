import sys
sys.setrecursionlimit(100000)


def dfs(graph, visited, x, y, color):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] != color:
        return False
    # 현재 노드를 아직 방문하지 않았고, 같은 색깔이라면
    if visited[x][y] == False:
        visited[x][y] = True
        dfs(graph, visited, x-1, y, color)
        dfs(graph, visited, x+1, y, color)
        dfs(graph, visited, x, y+1, color)
        dfs(graph, visited, x, y-1, color)
        return True
    return False


if __name__ == "__main__":
    n = int(input())

    # 그래프 입력받기
    graph_normal, graph_abnormal = [[]
                                    for _ in range(n)], [[] for _ in range(n)]
    for i in range(n):
        line = list(sys.stdin.readline().rstrip())
        for c in line:
            # 적록색약인 사람은 G와 R을 구분하지 못함
            if c == 'G':
                graph_abnormal[i].append('R')
            else:
                graph_abnormal[i].append(c)
            graph_normal[i].append(c)
    # 정상, 적록색약일 때 결과
    normal, abnormal = 0, 0

    # 방문 확인 테이블
    visited_normal = [[False] * (n+1) for _ in range(n+1)]
    visited_abnormal = [[False] * (n+1) for _ in range(n+1)]

    # 움직일 수 있는 방향
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    for i in range(n):
        for j in range(n):
            # 색약이 아닌 사람과 색약인 사람 구분 / 시작지점의 그래프 색깔을 parameter 지정
            if dfs(graph_normal, visited_normal, i, j, graph_normal[i][j]
                   ) == True:
                normal += 1
            if dfs(graph_abnormal, visited_abnormal, i, j, graph_abnormal[i][j]) == True:
                abnormal += 1
    print(normal, abnormal)
