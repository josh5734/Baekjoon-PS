import sys, heapq
input = sys.stdin.readline

def dijkstra(graph, start):
    distance = [int(1e10)] * (n+1) # 처음 거리는 모두 무한대로 초기화
    distance[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        currCost, currPos = heapq.heappop(pq)
        if currCost < distance[currPos]: continue

        for nextCost, nextPos in graph[currPos]:
            if currCost + nextCost < distance[nextPos]:
                distance[nextPos] = currCost + nextCost
                heapq.heappush(pq,(currCost+nextCost, nextPos))

    return distance

tc = int(input()) # 테스트 케이스의 개수
for _ in range(tc):
    n, m, t = map(int, input().split()) # 교차로, 도로, 목적지 후보의 개수
    s, g, h = map(int, input().split()) # s는 출발지이고 g,h는 냄새를 맡은 도로
    
    graph = [[] for _ in range(n+1)]
    dest = []
    g_to_h = 0
    for _ in range(m):
        a, b, d = map(int, input().split()) # a, b 사이에 거리가 d인 도로 존재
        graph[a].append((d,b))
        graph[b].append((d,a))
        if (a == g and b == h) or (a == h and b == g): g_to_h = d # g, h 사이의 거리

    for _ in range(t): dest.append(int(input())) # t개의 목적지 후보

    # (s -> d) = (s -> g) + (g -> h) + (h -> d)
    # (s -> d) = (s -> h) + (h -> g) + (g -> d)
    answer = []
    distance_s = dijkstra(graph, s) # 시작점 s로부터 다른 지점까지의 거리
    distance_g = dijkstra(graph, g) # 시작점 g로부터 다른 지점까지의 거리
    distance_h = dijkstra(graph, h) # 시작점 h로부터 다른 지점까지의 거리

    for d in dest:
        totalCost = distance_s[d]
        s_to_g, h_to_d = distance_s[g], distance_h[d]
        s_to_h, g_to_d = distance_s[h], distance_g[d]
        if totalCost == g_to_h + min(s_to_g + h_to_d, s_to_h + g_to_d):
            answer.append(d)
    for x in sorted(answer): print(x, end = " ")
