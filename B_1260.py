from collections import deque

# dfs


def dfs(graph, start, visited):

    # 현재 노드를 방문 처리
    visited[start] = True
    print(start, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):

    q = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 하나의 원소를 뽑아서 출력
        v = q.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된 아직 방문하지 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


# n, m, v 정보 입력받기
n, m, v = map(int, input().split())

# 그래프 생성
graph = [[] for i in range(n+1)]
for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# 작은 노드부터 방문하도록 재정렬
for x in graph:
    x = x.sort()

# 방문 여부 표시를 위한 visited
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

if __name__ == "__main__":

    dfs(graph, v, visited_dfs)
    print()
    bfs(graph, v, visited_bfs)
