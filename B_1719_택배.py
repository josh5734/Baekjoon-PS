import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(start):
    parents = defaultdict() # 각 지점의 이전 지점을 저장하는 리스트
    for i in range(1, n+1): parents[i] = i
    distance = [int(1e10)] * (n+1) # 각 지점까지의 거리를 저장하는 리스트
    distance[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        currCost, currPos = heapq.heappop(pq)
        # 이미 방문한 적이 있다면 무시
        if distance[currPos] < currCost: continue
        
        for next in graph[currPos]:
            nextCost, nextPos = next[0], next[1]
            if currCost + nextCost < distance[nextPos]:
                heapq.heappush(pq, (currCost + nextCost, nextPos))
                distance[nextPos] = currCost + nextCost
                parents[nextPos] = currPos
    # 각 지점에 가기 위해 첫번째로 방문하는 곳을 출력            
    for i in range(1, n+1):
        if i == start: # 목적지가 자신이면 "-" 출력
            print("-", end = " ")
        else: # 목적지가 다른 곳이면 parents에서 탐색
            curr = i
            while(parents[curr] != start):
                curr = parents[curr]
            print(str(curr), end = " ")
    print()

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

for i in range(1, n+1):
    dijkstra(i)

