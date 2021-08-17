import sys
import copy
sys.setrecursionlimit(1000000)


def dfs(x, y):  # dfs를 통해 같은 연합에 속하는 국가를 찾고, 인구 이동
    union.append([x, y])
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 이동가능하고, 아직 방문하지 않은
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            # 인구의 차이가 l보다 크고 r보다 작은 도시라면
            if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                dfs(nx, ny)


if __name__ == "__main__":
    n, l, r = map(int, input().split())

    graph = [[] for _ in range(n)]
    for i in range(n):  # 그래프 정보 입력
        graph[i] = list(map(int, sys.stdin.readline().split()))

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    answer = 0
    while True:
        visited = [[False] * n for _ in range(n)]  # i,j for loop를 다 돌때까지 1회 사용
        popMove = False  # 한 번이라도 인구이동이 일어나는지 확인하는 flag

        for i in range(n):
            for j in range(n):
                union = []
                if not visited[i][j]:  # 갱신된 인구가 다음 갱신에 영향 X
                    dfs(i, j)
                    if len(union) > 1:
                        popMove = True
                        population = sum([graph[x][y]
                                          for x, y in union]) // len(union)
                        for x, y in union:
                            graph[x][y] = population

        if not popMove:
            break
        answer += 1

    print(answer)
