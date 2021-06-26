import copy


def floyd_after_delete_edge(graph, i, j):
    INF = int(1e9)

    temp_graph = copy.deepcopy(graph)
    # 간선 삭제
    temp_graph[i][j] = INF
    temp_graph[j][i] = INF

    for k in range(N):
        for a in range(N):
            for b in range(N):
                temp_graph[a][b] = min(
                    temp_graph[a][b], temp_graph[a][k]+temp_graph[k][b])

    print(temp_graph)
    print()
    # print(after_graph)
    flag = True
    for i in range(N):
        for j in range(N):
            if temp_graph[i][j] != s_graph[i][j]:
                flag = False
                break
    if flag:
        print("시행")
        graph[i][j] = INF
        graph[j][i] = INF


if __name__ == "__main__":
    INF = int(1e9)
    # 도시의 수
    N = int(input())

    graph = [[] for _ in range(N)]
    # 각 간선에 대한 정보 입력받기
    for i in range(N):
        graph[i] = list(map(int, input().split()))

    s_graph = [[INF] * N for _ in range(N)]
    for k in range(N):
        for a in range(N):
            for b in range(N):
                s_graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    if s_graph != graph:
        print("-1")
    else:
        for i in range(N):
            for j in range(N):
                if i != j:
                    floyd_after_delete_edge(graph, i, j)
    print(graph)
