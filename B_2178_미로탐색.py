from collections import deque


def escape(graph, x, y):

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            # 이동
            x_after = x + dx[i]
            y_after = y + dy[i]

            # 미로 밖으로 벗어나지 않도록 하는 조건
            if x_after < 0 or y_after < 0 or x_after >= n or y_after >= m:
                continue

            # 벽인 경우 이동 안하도록
            if graph[x_after][y_after] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단거리 기록
            if graph[x_after][y_after] == 1:
                graph[x_after][y_after] = graph[x][y] + 1
                q.append((x_after, y_after))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]


if __name__ == "__main__":
    n, m = map(int, input().split())

    # 이동횟수
    moving = 0
    # 미로 정보를 그래프로 표현
    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))

    # 이동 방향 설정, up, down, left, right
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    print(escape(graph, 0, 0))
