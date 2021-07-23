import heapq
import sys


def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, curr = heapq.heappop(pq)
        if (distance[curr] < dist): continue; 
        
        for next in graph[curr]:
            cost = dist + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(pq, (cost, next[0]))


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    inf = int(1e10)

    distance = [inf] * (n+1)  # 시작 정점으로부터 다른 도시까지 거리
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        start, end, cost = map(int, sys.stdin.readline().split())
        graph[start].append((end, cost))

    start, dest = map(int, input().split())
    dijkstra(start)
    print(distance[dest])
