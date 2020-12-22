import heapq
import sys


def dijkstra(start):
    q = []
    # 시작 위치
    heapq.heappush(q, (0, start))
    distance[start] = 0
    visited[start] = True
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, node = heapq.heappop(q)
        # 방문한 노드 체크
        visited[node] = True

        # 현재 노드와 연결된 다른 인접 노드를 확인
        for i in graph[node]:
            # 방문하지 않은 노드에 대해서 최소거리 갱신
            if not visited[i[0]]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))


if __name__ == "__main__":
    INF = int(1e9)

    # 도시의 개수, 버스의 개수 입력받기
    N, E = int(input()), int(input())

    # 간선 정보를 담는 graph
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        sour, dest, cost = map(int, sys.stdin.readline().split())
        graph[sour].append((dest, cost))

    # 방문 내역 체크
    visited = [False] * (N + 1)

    # 최단 경로 테이블 초기화
    distance = [INF] * (N + 1)

    # 출발지, 도착지
    start, end = map(int, input().split())

    dijkstra(start)

    print(distance[end])
