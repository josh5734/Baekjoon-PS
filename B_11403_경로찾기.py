import sys


def dfs(start, graph, visited, first_visit):
    # 자기 자신은 처음에 바로 방문체크를 하지 않고 path가 존재할 때 방문체크를 한다.
    if first_visit:
        first_visit = False
    else:
        visited[start] = 1
    for i in range(N):
        if(visited[i] == 0 and graph[start][i] == 1):
            dfs(i, graph, visited, first_visit)

    return visited


if __name__ == "__main__":
    # 정점의 개수
    N = int(input())

    # 방향 그래프 입력 받기
    graph = [[] for _ in range(N)]
    for i in range(N):
        graph[i] = list(map(int, sys.stdin.readline().split()))

    # 경로를 표시할 Adjaceny matrix
    path = [[0] * N for _ in range(N)]

    for i in range(N):
        # 방문 여부를 체크 할 테이블 초기화
        visited = [0] * N
        # 첫 방문(자기 자신)일 때를 별도로 체크
        first_visit = True
        path[i] = dfs(i, graph, visited, first_visit)

    for i in range(N):
        for j in range(N):
            print(path[i][j], end=" ")
        print()
