import sys,heapq
from collections import defaultdict

def dijkstra(start):
    # 경로를 구하기 위한 부모 초기화
    for c in range(1, n+1):
        if c != start:
            parents[c] = None

    pq = []
    heapq.heappush(pq,(0, start))
    while pq:
        curr_cost, curr = heapq.heappop(pq)
        if distance[curr] < curr_cost:
            continue
        
        for next in graph[curr]:
            next_cost, next_node = next[0], next[1]
            
            if curr_cost + next_cost < distance[next_node]:
                heapq.heappush(pq, (curr_cost + next_cost, next_node))
                distance[next_node] = curr_cost + next_cost
                
                # 현재 노드를 다음 노드의 부모로 지정한다.
                parents[next_node] = curr                

    # 시작부터 끝점까지 경로 생성하기
    route = []
    current = end
    while current != start:
        route.append(current)
        current = parents[current]
    route.append(start)
    route.reverse()
    return route



    return route
input = sys.stdin.readline
inf = int(1e9)

n, m = int(input()), int(input())
# 간선 정보 입력하기
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, cost = map(int, input().split())
    graph[s].append((cost, e))

# 시작점, 도착점 정보 입력받기
start, end = map(int, input().split())

# 출발 도시부터 다른 도시까지 최단 거리를 저장하는 리스트
distance = [inf] * (n+1)
distance[start] = 0

# 경로 추적을 위한 딕셔너리
parents = defaultdict()

route = dijkstra(start)
print(distance[end])
print(len(route))
print(*route)