import sys, heapq

inf = int(1e10)
n, m, x = map(int, input().split())

def dijkstra(start, end):
    distance = [inf] * (n+1)
    distance[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        dist, now = heapq.heappop(pq)
        for next in graph[now]:
            cost = dist + next[0]
            if distance[next[1]] > cost:
                distance[next[1]] = cost
                heapq.heappush(pq, (cost, next[1]))
    return distance[end]


graph = [[] for _ in range(n+1)]
answer = 0
for _ in range(m):
    sour, dest, cost = map(int, sys.stdin.readline().split())
    graph[sour].append((cost,dest))

distance = [0] * (n+1)
for i in range(1, n+1):
    distance[i] = dijkstra(i, x) + dijkstra(x, i)
    if distance[i] > answer:
        answer = distance[i]
print(answer)
