import sys
import heapq


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


if __name__ == "__main__":
    # 거리를 무한대로 초기화하기 위함
    INF = int(1e9)

    # 정점, 간선 개수
    n, e = map(int, input().split())

    # 시작점
    start = 1

    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
    graph = [[] for i in range(n+1)]
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n + 1)

    # 모든 간선 정보 입력받기
    for _ in range(e):
        sour, dest, cost = map(int, sys.stdin.readline().split())
        # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
        graph[sour].append((dest, cost))
        graph[dest].append((sour, cost))

    # 반드시 지나야 하는 두 정점
    node1, node2 = map(int, input().split())

    total_distance1, total_distance2 = 0, 0
    way1, way2 = [start, node1, node2, n], [start, node2, node1, n]

    # 시작점 -> node1 -> node2 -> 목적지
    for x in range(3):
        dijkstra(way1[x])
        total_distance1 += distance[way1[x+1]]
        distance = [INF] * (n + 1)

    # 시작점 -> node2 -> node1 -> 목적지
    for x in range(3):
        dijkstra(way2[x])
        total_distance2 += distance[way2[x+1]]
        distance = [INF] * (n + 1)

    min_distance = min(total_distance1, total_distance2)

    # 경로 중에서 갈 수 없는 곳이 있었다면 INF가 더해짐
    if min_distance >= INF:
        print(-1)
    else:
        print(min_distance)
