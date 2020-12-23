from collections import deque


def topology_sort():
    q = deque()

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if(indegree[i] == 0):
            q.append(i)

    # 모든 노드에 대해서 방문
    for i in range(1, n+1):
        # 시작 노드를 큐에서 뺀 뒤 result에 기록
        start = q.popleft()
        result[i] = start

        # 시작 노드로부터 연결된 지점에 대해서
        for j in graph[start]:
            end = j
            # 간선을 삭제하며 진입차수를 감소시킴
            indegree[end] -= 1
            # 만약 진입차수가 0이 되는 노드가 생기면 다시 큐에 삽입
            if indegree[end] == 0:
                q.append(end)

    # 결과 출력
    for i in range(1, n+1):
        print(result[i], end=" ")


if __name__ == "__main__":
    n, e = map(int, input().split())

    # 진입차수를 기록
    indegree = [0] * (n+1)
    # 결과를 담을 리스트
    result = [0] * (n+1)

    # 간선의 순서 정보를 담는 그래프
    graph = [[] for _ in range(n+1)]

    # 연결된 간선 정보를 입력하고, 방향그래프의 도착지쪽의 진입차수를 증가시킴
    for _ in range(e):
        start, end = map(int, input().split())
        graph[start].append(end)
        indegree[end] += 1

    topology_sort()
