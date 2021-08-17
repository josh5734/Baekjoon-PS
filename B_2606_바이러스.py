
def dfs(graph, start, visited, infected):
    # 방문한 노드를 체크
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            infected += 1
            dfs(graph, i, visited, infected)


# main #
if __name__ == "__main__":
    # n, m 입력받기
    n = int(input())
    m = int(input())

    # 그래프 정보 입력
    graph = [[] for i in range(n+1)]
    for i in range(m):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    visited = [False] * (n + 1)
    infected = 0

    dfs(graph, 1, visited, infected)
    print(infected)
